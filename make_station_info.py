import pandas as pd
import csv
import geopy


station_info = pd.read_csv('station_web_info.csv')

station_info['Timezone'] = '***'  # initialize
stations_by_state = station_info.groupby('State')

with open('timezones_by_state.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        rows_to_change = stations_by_state.get_group(row['STATE']).index
        station_info.loc[rows_to_change, 'Timezone'] = row['TIMEZONE']

# now have all the timezones that can be looked up by state
# next, have to look up individual station timezones with geocoding
#   for unknown timezones ('***')

stations_by_timezone = station_info.groupby('Timezone')

rows_to_geocode = stations_by_timezone.get_group('***').index
print('{} rows to geocode.'.format(len(rows_to_geocode)))

from geopy.geocoders import GoogleV3

for i in rows_to_geocode:
    lat = station_info.loc[i, 'Latitude']
    lon = station_info.loc[i, 'Longitude']
    try:
        st_timezone = GoogleV3().timezone((lat, lon)).zone
    except:
        print('ERROR: Could not get timezone for {}, {}'.format(
               station_info.loc[i, 'StationName'],
               station_info.loc[i, 'State']))
        station_info.loc[i, 'Timezone'] = 'UNKNOWN'
    else:
        station_info.loc[i, 'Timezone'] = st_timezone
        print('Geocoded {}, {} to timezone {}'.format(
               station_info.loc[i, 'StationName'],
               station_info.loc[i, 'State'], st_timezone))

station_info.to_csv('station_info.csv', index=False)

stations_by_timezone = station_info.groupby('Timezone')

print('Done, with the following missing timezones:')
print(repr(stations_by_timezone.get_group('UNKNOWN')))

# Will go through the csv output by hand and fill in UNKNOWN values
