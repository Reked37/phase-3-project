from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Website(Base):
    __tablename__ = 'websites'

    id= Column(Integer(), primary_key=True)
    website=Column(String())
    username= Column(String())
    password= Column(String())

    website_users= relationship('WebsiteUser', back_populates='website')

    def __repr__(self):
        return f'Website(id={self.id},' + \
        f'website={self.website},' + \
        f'username={self.username},' + \
        f'password={self.password})'

class User(Base):
    __tablename__= 'users'

    id= Column(Integer(), primary_key=True)
    name_of_user= Column(String())
    web_browser= Column(String())

    website_users= relationship('WebsiteUser', back_populates='user')

    def __repr__(self):
        return f'User(id={self.id},' + \
        f'name_of_user={self.user},' + \
        f'web_browser={self.web_browser})'

class WebsiteUser(Base):
    __tablename__= 'website_users'

    id= Column(Integer(), primary_key=True)
    website_id = Column(ForeignKey('websites.id'))
    user_id = Column(ForeignKey('users.id'))

    website= relationship('Website', back_populates='website_users')
    user= relationship('User', back_populates='website_users')

    def __repr__(self):
        return f'WebsiteUser(id={self.id},' + \
        f'website_id={self.website_id},' + \
        f'user_id={self.user_id})'





