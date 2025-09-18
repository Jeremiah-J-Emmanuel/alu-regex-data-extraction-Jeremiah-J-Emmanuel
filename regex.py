#!/usr/bin/ env python3
import re # The library for regular expressions


def prompt_user():
    print("Please select the type of data that you want to validate:")
    print("1. Emails")
    print("2. Phone numbers")
    print("3. URLS")
    print("4. Credit Card Numbers")
    print("5. html tags")
    
    while True: # A while loop is used for input validation.
        selection = input("Select 1-5: ").strip()
        if selection == "1":
            ...
            break
        elif selection == "2":
            ...
            break
        elif selection == "3":
            ...
            break
        elif selection == "4":
            ...
            break
        elif selection == "5":
            ...
            break
        else:
            print("Please select the numbers 1-5!")
            continue
    