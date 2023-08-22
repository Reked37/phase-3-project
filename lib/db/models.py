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

# class WebsiteUser(Base):
#     __tablename__= 'website_users'

#     id= Column(Integer(), primary_key=True)

#     def __repr__(self):
#         return f'WebsiteUser(id={self.id},' + \
#         f'website_id={self.website_id},' + \
#         f'user_id={self.user_id})'





