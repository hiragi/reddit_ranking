# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2
import os

URL = "http://www.reddit.com/top/"

html = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html)

def scrape():
	"""
	scraping article title

	Returns:
		title as array
	"""

	ret = []

	# Scrape title
	title = (soup("p", {"class": "title"}))

	for name in title:
		for atag in name.findAll("a"):
			ret.append(atag.renderContents())
	
	return ret

def main():
	for i, title in enumerate(scrape()):
		if i % 2 == 0:
			print("%2.i\t%s" % (i/2+1, title))
			print

if __name__ == "__main__":
	os.system("clear")
	main()
