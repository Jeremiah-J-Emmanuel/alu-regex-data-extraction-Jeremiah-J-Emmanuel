#!/usr/bin/ env python3
import re # The library for regular expressions
import time
import os


def clear_screen():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  #For Linux/macOS
        _ = os.system('clear')

def prompt_user():
    clear_screen()
    try:
        print("Please select the type of data that you want to validate:")
        print("1. Emails")
        print("2. Phone numbers")
        print("3. URLS")
        print("4. Credit Card Numbers")
        print("5. html tags")
        print("6. Time")
    
        while True: # A while loop is used for input validation.
            selection = input("Select 1-6: ").strip()
            if selection == "1":
                email()
                continue_or_stop()
                break
            elif selection == "2":
                phone_number()
                continue_or_stop()
                break
            elif selection == "3":
                url()
                continue_or_stop()
                break
            elif selection == "4":
                credit_card()
                continue_or_stop()
                break
            elif selection == "5":
                html_tags()
                continue_or_stop()
                break
            elif selection == "6":
                time_check()
                continue_or_stop()
            else:
                print("Please select the numbers 1-5!")
                continue

    except KeyboardInterrupt:
        clear_screen()
        print("Shutting down application...")
        time.sleep(1.5)

    except Exception as e:
        print(f"An error, {e}, has occured, attempting restart now...")
        time.sleep(2)
        prompt_user()

def email():
    clear_screen()
    while True:
        quote = input("\nEnter the Email: ").strip()
        output = re.findall("^[A-Za-z0-9][\w_.-]+[A-Za-z0-9]@([A-Za-z0-9][A-Za-z0-9-]+.)+[A-Za-z]{2,}$", quote)
        if output:
            print(f"The Email, {quote}, input is correct!")
            break
        else:
            print(f"The Email, {quote}, is not correct! Please try again!")
            print("Emails should follow this format: user@example.com or firstname.lastname@company.co.uk")
            continue


def phone_number():
    clear_screen()
    while True:
        quote = input("\nEnter the phone number: ").strip()
        output = re.findall("^(\(?\d{3}\)?)(-| |\.)\d{3}(-| |\.)\d{4}$", quote)
        if output:
            print(f"The phone number, {quote}, is correct!")
            break
        else:
            print(f"The phone number, {quote}, entered is not correct! Please try again!")
            print("Phone numbers should follow these formats: (123) 456-7890 or 123-456-7890 or 123.456.7890 \n")
            continue


def url():
    clear_screen()
    while True:
        quote = input("\nEnter the URL: ").strip()
        output = re.findall("(https:\/\/|http:\/\/)(www\.)?(\w+(-)*\w+\.)+\w+(\/(\w+)?)*(\?\w+=\w+)*$", quote)
        if output:
            print(f"The URL, {quote}, input is correct!")
            break
        else:
            print(f"The URL, {quote}, is not correct! Please try again!")
            print(f"The URL should follow these formats: https://www.example.com or https://subdomain.example.org/page \n")
            continue


def credit_card():
    clear_screen()
    while True:
        quote = input("\nEnter the credit card number: ").strip()
        output = re.findall("^\d{4}(-| )?\d{4}(-| )?\d{4}(-| )?\d{4}$", quote)
        if output:
            print(f"The credit card number, {quote}, is correct!")
            break
        else:
            print(f"The credit card number, {quote}, entered is not correct! Please try again!")
            print("Phone numbers should follow these formats: 1234 5678 9012 3456 1234-5678-9012-3456\n")
            continue


def html_tags():
    clear_screen()
    while True:
        quote = input("\nEnter the HTML tag: ").strip()
        output = re.findall("^<([A-Za-z][\w\-]*)((( )+[A-Za-z-]+)(=((\"[\w\-\. ]+\")|('[\w\-\. ]+'))))*>$", quote)
        if output:
            print(f"The HTML tag, {quote}, is correct!")
            break
        else:
            print(f"The HTML tag, {quote}, entered is not correct! Please try again!")
            print("HTML tags should follow these formats: <p> <div class=\"example\"> <img src=\"image.jpg\" alt=\"description\">\n")
            continue

    
def time_check():
    clear_screen()
    while True:
        quote = input("\nEnter the time (24hr format or 12hr format): ").strip().upper()
        output = re.findall("((23|22|21|20|([0-1][0-9])):[0-5]\d)|((12|11|10|[1-9]):[0-5]\d (AM|PM))", quote)
        if output:
            print(f"The time, {quote}, is correct!")
            break
        else:
            print(f"The time, {quote}, entered is not correct! Please try again!")
            print("The entered time should follow these formats: 14:30 (24-hour format) or 2:30 PM (12-hour format)")


def continue_or_stop():
    while True:
        ans = input("\nDo you want to continue validating input [Y/N]: ").strip().lower()
        if ans == "y":
            clear_screen()
            print("Continuing to validate data...")
            time.sleep(1)
            clear_screen()
            prompt_user()
            break
        elif ans == "n":
            clear_screen
            print("Closing application now...")
            time.sleep(1.5)
            break
        else:
            print("Enter Y or N")
            continue



if __name__ == "__main__":
    prompt_user()