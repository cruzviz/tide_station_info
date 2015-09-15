# tide_station_info
Scrape NOAA tide station listings and create the station_info.csv file for the Sun * Moon * Tide calendar maker.

## Order of files to run:
0. webscrape1.py
1. get_hrefs.py
2. scrape_by_state.py
3. make_station_info.py

timezones_by_state.csv was hand created to save some geocoding. It allows make_station_info to insert timezones automatically for states that are all in one timezone. The geocoding only happens for stations in states that cover more than one timezone.
