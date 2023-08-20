from functions.create import add_to_database
from functions.delete import delete_from_database
from functions.search import look_for_entry
from functions.change import look_in_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def main_menu():
    print('Welcome to my phase 3 project!')
    user_or_website=input("Type in 'Add' to add a user or 'Website' to enter login info ").lower()
    
    if user_or_website == 'add':
        add_user()
    elif user_or_website == 'website':
        website_login_details()

    
def website_login_details():
    decision= input("Type in 'Create' for new entry, 'Search' for password, 'Change' to modify an entry, or 'Delete' to delete an entry ")
    if decision == 'create':
        add_to_database()
    elif decision == 'search':
        look_for_entry()
    elif decision == 'change':
        look_in_database()
    elif decision == 'delete':
        delete_from_database()
    else:
        print(f'{choice} is not a valid choice')

def add_user():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()

    username=input("What's your username? ")
    web_browser=input("What web browser do you use? ")

    entry= User(name_of_user=username, web_browser=web_browser)
    session.add(entry)
    session.commit()
    print(f'{entry.name_of_user} has been added!')
    session.close()
    