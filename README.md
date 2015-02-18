EduScrape
================
EduScrapte is a simple scraper program that mimics a browser with Splinter to scrape the Coursera courses page, parses the reponse with Beautiful Soup according to a course schema, and utillizes a data pipeline to store individual course details in PostgreSQL.

###Contents
<ul>
	<li><a href="#technologies-and-stack">Technologies & Stack</a></li>
	<li><a href="#features">Features</a></li>
	<li><a href="#forking">Forking</a></li>
</ul>


Technologies and Stack
------------------------
<h4>Backend:</h4>
Python<br>
Python libraries: BeautifulSoup, Splinter<br>
PostgreSQL<br>
SQLAlchemy<br>
Data scraping: 
Data cleaning, sorting: 
Data modeling: 


Features
-------------------
#####Scraping
- [X] 
- [X] 

#####Data Modeling
- [X] 
- [X] 


Forking?
-----------------------
Clone my repository and navigate to the project folder.

	`$ curl git@github.com:MarsWilliams/EduScraper.git`
	`$ cd EduScraper`


Install dependencies.

	`$ pip install -r requirements.txt`


You'll need to install PostgreSQL.

	`$ curl https://github.com/PostgresApp/PostgresApp/releases/download/9.4.1.0/Postgres-9.4.1.0.zip"`

	
Launch PostgreSQL.

	click on the package after download, and follow the installation prompts

	open the app (you should see an elephant symbol in your task bar)


Create the database.

	`$ psql -h localhost -d postgres`
	`$ postgres=# create database courses`


Run the spider.

	`$ python spider.py`


Play with the data!

	`$ psql -h localhost -d postgres`
	`$ postgres=# select * from courses limit 5`


I'm happy to answer any questions you may have or help with installation.

![lovely](https://cloud.githubusercontent.com/assets/6811339/5433884/6ed29e24-8400-11e4-906d-cb4bec19b8e4.png)



