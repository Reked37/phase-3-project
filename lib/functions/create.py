from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Website, Browser

def create_new_entry(session, valid_website, username, password, valid_browser):
    #dictionary
    new_entry={'username': username, 'password': password, 'website_id':valid_website.id, 'browser_id': valid_browser.id}
    session.add(User(**new_entry))
    session.commit()
    return new_entry

def add_to_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()
    
    valid_browser=verify_browser(session)
    valid_website=verify_website(session)

    username=input('Username: ')
    password=input('Password: ')
    entry=create_new_entry(session, valid_website, username, password, valid_browser)
    print("New entry created!")
    session.close()

def verify_browser(session):
    list_of_valid_browsers=[]
    all_browsers=session.query(Browser).all()
    if all_browsers:
        for browser in all_browsers:
            list_of_valid_browsers.append(browser.browser_name)
    print(list_of_valid_browsers)
    entered_browser=input('What browser do you prefer? ')
    valid_browser= session.query(Browser).filter_by(browser_name=entered_browser).first()
    if not valid_browser:
        print(f'{entered_browser} is not a valid browser')
        verify_browser(session)
    return valid_browser

def verify_website(session):
    list_of_valid_sites=[]
    all_sites=session.query(Website).all()
    if all_sites:
        for website in all_sites:
            list_of_valid_sites.append(website.website)
    print(list_of_valid_sites)
    website_name=input('Name of website: ')
    valid_website=session.query(Website).filter_by(website=website_name).first()
    if not valid_website:
        print(f'{website_name} is not a valid website')
        verify_website(session)
    return valid_website
        

