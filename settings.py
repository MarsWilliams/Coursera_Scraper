#! -*- coding: utf-8 -*-

"""
Coursera Course Scraper Project

Scrape data from a regularly updated website coursera.com and
save to a database (postgres).

Scrapy settings part - defines settings for the Coursera Course Scraper Project.
"""

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'marswilliams',
	'password': 'Weareallg0ds!',
	'database': 'courses'
}

ITEM_PIPELINES = {'coursera_scrape.pipelines.CourseraPipeline': 1}

USER_AGENT = 'coursera_scrape (+http://cargocollective.com/metaphor_formation)'
