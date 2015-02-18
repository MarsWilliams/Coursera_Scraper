! -*- coding: utf-8 -*-

"""
Coursera Course Scraper Project

Scrape data from a regularly updated website coursera.com and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.dialects import postgresql

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))


def create_courses_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Courses(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    organization = Column('organization', String)
    title = Column('title', String)
    authors = Column('authors', postgresql.ARRAY(String))
    start_date = Column('start_date', Integer, nullable=True)
    duration = Column('duration', Integer, nullable=True)
