from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Website(Base):
    __tablename__ = 'websites'

    id= Column(Integer(), primary_key=True)
    website=Column(String())
    username= Column(String())
    password= Column(String())

    def __repr__(self):
        return f'Website(id={self.id},' + \
        f'website={self.website},' + \
        f'username={self.username},' + \
        f'password={self.password})'

# class User(Base):
#     __tablename__: 'users'

#     id= Column(Integer(), priamry_key=True)
#     user= Column(String())

# class UserWebsite(Base):
#     __tablename__: 'UserWebsite'

#     id= Column(Integer(), primary_key=True)
