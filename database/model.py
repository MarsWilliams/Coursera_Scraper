# ! -*- coding: utf-8 -*-

"""
Coursera Course Scraper Project

Scrape data from a regularly updated website coursera.com and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker, scoped_session
import settings


DeclarativeBase = declarative_base()

ENGINE = create_engine(URL(**settings.DATABASE), echo=True)

Session = scoped_session(sessionmaker(bind=ENGINE,
                                        autocommit = False,
                                        autoflush = False))

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine(URL(**settings.DATABASE), echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()


def create_courses_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Course(DeclarativeBase):
    """SQLAlchemy courses model"""
    __tablename__ = "course_details"

    id = Column(Integer, primary_key=True)
    organization = Column('organization', String)
    title = Column('title', String)
    authors = Column('authors', String)
    start_date = Column('start_date', Date(timezone=False), nullable=True)
    end_date = Column('end_date', Date(timezone=False), nullable=True)
    duration = Column('duration', String, nullable=True)
    schedule_notes = Column('schedule_notes', String, nullable=True)
