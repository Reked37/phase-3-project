from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Website, Browser

def create_new_entry(session, website_name, username, password, entered_browser):
    valid_website=session.query(Website).filter_by(website=website_name).first()
    valid_browser= session.query(Browser).filter_by(browser_name=entered_browser).first()

    if not valid_website:
        print(f'{website_name} is not a valid website')

    if not valid_browser:
        print(f'{entered_browser} is not a valid browser')

    #dictionary
    new_entry={'website_name': website_name, 'username': username, 'password': password, 'website_id':valid_website.id, 'browser_id': valid_browser.id}
    session.add(User(**new_entry))
    session.commit()
    return new_entry

def add_to_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()

    entered_browser=input('What browser do you prefer? ')
    website_name=input('Name of website: ')
    username=input('Username: ')
    password=input('Password: ')

    entry=create_new_entry(session, website_name, username, password, entered_browser)

    print("New entry created!")

    session.close()





