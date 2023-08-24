from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id= Column(Integer(), primary_key=True)
    website_name= Column(String())
    username= Column(String())
    password= Column(String())
    website_id= Column(Integer(), ForeignKey('websites.id'))
    browser_id= Column(Integer(), ForeignKey('browsers.id'))

    def __repr__(self):
        return f'User(id={self.id},' + \
        f'website_name={self.website_name},' + \
        f'username={self.username},' + \
        f'password={self.password})'

class Website(Base):
    __tablename__= 'websites'

    id= Column(Integer(), primary_key=True)
    website= Column(String())
    created= Column(DateTime())

    #user belong to a specific website
    users= relationship('User', backref=backref('website'))

    def __repr__(self):
        return f'Website(id={self.id},' + \
        f'website={self.website},' + \
        f'created={self.created})'

class Browser(Base):
    __tablename__='browsers'

    id= Column(Integer(), primary_key=True)
    browser_name= Column(String())
    company= Column(String())

    preferred_browser= relationship('User', backref=backref('browser'))






