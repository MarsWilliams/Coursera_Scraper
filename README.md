EduScrape
================
EduScrapte is a simple scraper program that mimics a browser with Splinter to scrape the Coursera courses page, parses the reponse with Beautiful Soup according to a course schema, and utillizes a data pipeline to store individual course details in PostgreSQL.

###Contents
<ul>
	<li><a href="#technologies-and-stack">Technologies and Stack</a></li>
	<li><a href="#features">Features</a></li>
	<li><a href="#forking">Forking</a></li>
</ul>


Technologies and Stack
------------------------
Language: Python<br>
Data scraping: BeautifulSoup, Splinter <br>
Data modeling: SQLAlchemy <br>
Database: PostgreSQL


Features
-------------------
#####Scraping
- [X] Uses splinter to mimic browser behavior
- [X] Waits for content to laod before scraping

#####Data Modeling
- [X] Defines schema with SQLAlchemy
- [X] Content stored in PostgreSQL


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


Create the database and table.

	`$ psql -h localhost -d postgres`
	`$ postgres=# create database coursera`
	`$ postgres=# \connect coursera`
	`$ coursera=# CREATE TABLE course_details (id serial primary key not null, organization text, title text, authors text, start_date date, end_date date, duration text, schedule_notes text);`
	`$ coursera=# INSERT INTO course_details (organization, title, authors, start_date, end_date, duration, schedule_notes) VALUES ('Dummy Entry', None, None, now(), now(), None, None);`


Run the spider.

	`$ python spider.py`

Seed the database.

	`$ python seed.py`

Erase dummy data.

	`$ DELETE FROM course_details where organization='Dummy Entry'`	

Play with the data!

	`$ psql -h localhost -d postgres`
	`$ postgres=# SELECT * FROM course_details WHERE title LIKE '%Game%'`


I'm happy to answer any questions you may have or help with installation.


To Do
-----------------------
- [X] Create separate schema for authors
- [X] Write unit tests

![lovely](https://cloud.githubusercontent.com/assets/6811339/5433884/6ed29e24-8400-11e4-906d-cb4bec19b8e4.png)



