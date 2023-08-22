from faker import Faker
from faker.providers import date_time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Website, User
import random

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine)
session= Session()
fake=Faker()
# website_count=session.query(Website).count()

def delete_table():
  session.query(Website).delete()
  session.query(User).delete()
  session.commit()

def create_records():
    titles_of_websites=['Twitter', 'Facebook', 'Twitch', 'Youtube', 'Kick']
    websites=[]
    for website_name in titles_of_websites:
       website=Website(website=website_name, created=fake.date_time())
       session.add(website)
       session.commit()
       websites.append(website)

    users=[
        User(username='Reked', password='idk', website_id=websites[0].id, website_name='Twitter'),
        User(username='bluefin', password='penguin', website_id=websites[1].id, website_name='Facebook'),
        User(username='Cleo', password='thedog', website_id=websites[1].id, website_name='Facebook'),
        User(username='Rusty', password='corgi', website_id=websites[0].id, website_name='Twitter')
    ]
    session.add_all(users)
    session.commit()
    session.close()
    return websites, users

if __name__ == '__main__':
    delete_table()
    websites, users = create_records()
