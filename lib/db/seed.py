from faker import Faker
from faker.providers import date_time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Website, User, Browser
import random

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine)
session= Session()
fake=Faker()
# website_count=session.query(Website).count()

def delete_table():
  session.query(Website).delete()
  session.query(User).delete()
  session.query(Browser).delete()
  session.commit()

def create_records():
    #tuples
    titles_of_websites=('Twitter', 'Facebook', 'Twitch', 'Youtube', 'Kick')
    websites=[]
    for website_name in titles_of_websites:
       website=Website(website=website_name, created=fake.date_time())
       session.add(website)
       session.commit()
       websites.append(website)

    browser_list=['Chrome', 'Firefox', 'Safari', 'Internet Explorer']
    company_list=['Google', 'Mozilla', 'Apple', 'Microsoft']
    browsers=[]
    for browser_name, company_name in zip(browser_list, company_list):
        browser= Browser(browser_name=browser_name, company=company_name)
        session.add(browser)
        session.commit()
        browsers.append(browser)
    

    users=[
        User(username='Reked', password='idk', website_id=websites[0].id, website_name='Twitter', browser_id=browsers[0].id),
        User(username='bluefin', password='penguin', website_id=websites[1].id, website_name='Facebook', browser_id=browsers[3].id),
        User(username='Cleo', password='thedog', website_id=websites[1].id, website_name='Facebook', browser_id=browsers[1].id),
        User(username='Rusty', password='corgi', website_id=websites[0].id, website_name='Twitter', browser_id=browsers[0].id)
    ]
    session.add_all(users)
    session.commit()
    session.close()
    return websites, users, browsers

if __name__ == '__main__':
    delete_table()
    websites, users, browsers = create_records()
