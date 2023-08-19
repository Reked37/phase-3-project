#!/usr/bin/env python3
# import fire
from helpers import main_menu, decision
from models import Website



if __name__ == "__main__":
    main_menu()
    choice= input('Type in your choice: ')
    decision(choice)