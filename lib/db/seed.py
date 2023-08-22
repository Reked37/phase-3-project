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
    titles_of_websites=['Twitter', 'Kick']
    websites=[]
    for website_name in titles_of_websites:
       website=Website(website=website_name, created=fake.date_time())
       session.add(website)
       session.commit()
       websites.append(website)

    list_of_users=[]
    users=[
        User(username='Reked', password=12345, website_id=websites[0].id),
        User(username='bluefin', password='penguin', website_id=websites[1].id),
        User(username='Cleo', password='thedog', website_id=websites[1].id),
        User(username='Rusty', password='corgi', website_id=websites[0].id)
    ]
    session.add_all(users)
    session.commit()
    session.close()
    return websites, users

if __name__ == '__main__':
    delete_table()
    websites, users = create_records()
