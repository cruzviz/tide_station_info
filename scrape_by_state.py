import requests
import bs4
import csv


states = []
urls = []

with open('hrefs.txt', 'r') as file:
    for line in file:
        urls.append(line.split('\"')[1])
        temp = line.split('>')[1]
        states.append(temp.split('<')[0])

index = 'http://tidesandcurrents.noaa.gov/tide_predictions.html'
station_info = []

for i in range(0,len(states)):
    try:
        response = requests.get(index + urls[i])
        soup = bs4.BeautifulSoup(response.text)
        rows = soup.find_all('tr')
    except:
        print('Error getting table for {}'.format(states[i]))
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 2:  # ignore subheader rows
             st_name = cols[0].get_text().strip().title()
             st_id = cols[1].get_text()
             st_lat = cols[2].get_text()
             st_lon = cols[3].get_text()
             st_type = cols[4].get_text()
             state = states[i]
             station_info.append((st_id, st_name, state,
                    st_lat, st_lon, st_type))

    print('Done with {}'.format(states[i]))


header = ['StationID', 'StationName', 'State', 'Latitude', 
          'Longitude', 'StationType']

with open('station_web_info.csv', 'w', newline='') as file:
    f_csv = csv.writer(file)
    f_csv.writerow(header)
    f_csv.writerows(station_info)

