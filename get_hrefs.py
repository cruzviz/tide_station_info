import bs4
import re

f = open('soup1.txt', 'r')
soup = bs4.BeautifulSoup(f.read())
f.close

soup2 = soup.find_all(href = re.compile('gid=\d(?!\#)'))

with open('hrefs.txt', 'w') as file:
	for stuff in soup2:
		file.write("{}\n".format(stuff))

'''
I tried to make a regex to ignore #listing hrefs, but it doesn't work.
It just returns all the gid= hrefs.
I have to manually delete the extra hrefs with #listing from hrefs.txt,
but they are all together on top, so it isn't a big deal.
I also manually replaced a funky ampersand with 'and' in Lesser Antilles
and Virgin Islands.
'''
