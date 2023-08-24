from functions.create import add_to_database
from functions.delete import delete_from_database
from functions.search import look_for_entry
from functions.change import look_in_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Website
from datetime import datetime

def main_menu():
    print('Welcome to my phase 3 project!')
    user_or_website=input("Type in 'User' to enter a user interface or 'Website' to add a website ").lower()
    
    if user_or_website == 'user':
        user_interface()
    elif user_or_website == 'website':
        add_website()

    
def user_interface():
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

def add_website():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()

    new_website=input("Name of website: ")
    date_created=input("Enter date that the website was created? YYYY-MM-DD. ")
    format_date=datetime.strptime(date_created, '%Y-%m-%d')

    entry= Website(website=new_website, created=format_date)
    session.add(entry)
    session.commit()
    print(f'{entry.website} has been added!')
    session.close()
    