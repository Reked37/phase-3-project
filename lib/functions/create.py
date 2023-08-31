from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Website, Browser

def create_new_entry(session, valid_website, username, password, valid_browser):
    #dictionary
    new_entry={'username': username, 'password': password, 'website_id': valid_website.id, 'browser_id': valid_browser.id}
    session.add(User(**new_entry))
    session.commit()
    return new_entry

def add_to_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()
    
    username=input("What's the username to the website: ")

    if username == 'back':
        return
    else:
      password=input("What's the password to the site: ")
      valid_website=verify_website(session)
      valid_browser=verify_browser(session)
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

    while True:
      entered_browser=input('What browser do you prefer? ')
      valid_browser= session.query(Browser).filter_by(browser_name=entered_browser).first()
      if valid_browser:
          return valid_browser
      else:
          print(f'{entered_browser} is not a valid browser')
          
def verify_website(session):
    list_of_valid_sites=[]
    all_sites=session.query(Website).all()
    if all_sites:
        for website in all_sites:
            list_of_valid_sites.append(website.website)
    print(list_of_valid_sites)

    while True:
      website_name=input('Name of website: ')
      valid_website=session.query(Website).filter_by(website=website_name).first()
      if  valid_website:
          return valid_website
      else:
          print(f'{website_name} is not a valid website')
          
        

