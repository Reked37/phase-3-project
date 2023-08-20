from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Website, User, WebsiteUser

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine)
session= Session()
fake=Faker()

def delete_table():
    session.query(Website).delete()
    session.query(User).delete()
    session.commit()

def create_records():
    website_example=Website(
        website='Twitter',
        username='Tweet',
        password='XTwitter'
    )

    websites=[Website(
        website= fake.name(),
        username= fake.name(),
        password= fake.name()
    ) for i in range(10)]
    users=[User(
        name_of_user=fake.name(),
        web_browser=fake.name()
    ) for i in range(10)]

    website_users=[WebsiteUser(
        website=websites[i],
        user=users[i]
    ) for i in range(10)]

    session.add_all(websites + users + website_users)
    session.commit()
    return websites, users, website_users, website_example

if __name__ == '__main__':
    delete_table()
    websites, users, website_users, website_example = create_records()
