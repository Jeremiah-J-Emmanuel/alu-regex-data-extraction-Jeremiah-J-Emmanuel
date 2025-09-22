# alu-regex-data-extraction-Jeremiah-J-Emmanuel
------------------------------------------------------------------------------------------------
# Project Overview
This is for the individual formative lab, the Regex onboarding hackathon, at the African Leadership University.
This is a Python based code that validates phone numbers urls, credit card numnbers, html tags, and time in 24hr or 12hr format. It makes use of regex to validate user input.

# SETUP INSTRUCTIONS
To make use of this data validator, follow these steps.

1. Clone this repository:<br>
    a. If you are making use of a linux system, run this in your terminal:<br>
        git clone https://github.com/Jeremiah-J-Emmanuel/alu-regex-data-extraction-Jeremiah-J-Emmanuel.git <br>

        After cloning, go to the folder where the files are. The folder would most likely be called alu-regex-data-extraction-Jeremiah-J-Emmanuel
    b. If you are making use of an IDE like VS code or Atom to clone this repository:<br>
        Clone this repo with your IDE. Cloning methods vary for different IDEs

2. Run the code:<br>
    a. If you are making use of a linux system:
        Navigate into the folder of the clone repo. 
        Run this on your terminal: python3 regex.py<br>
        NOTE: Please do ensure that you have python3 installed.<br>
        If you have an older version of python that supports Regex, you may use it.
    
    b. If you are making use of an IDE:
        Run the code in the IDE

# HOW TO USE
When you run the code, you will be prompted to choose the type of input that you want to validate. If you do not choose from the options, you will be prompted to choose again. You will continue to be prompted until you choose a valid option. 


Example:<br>
<strong>
Please select the type of data that you want to validate:
1. Emails
2. Phone numbers
3. URLS
4. Credit Card Numbers
5. html tags
6. Time
Select 1-6: 
</strong>

When you choose an option, you will be asked to input the data that you want to validate. If the input that you have entered is not valid, you will be reprompted to enter a valid input:

Example:
Assuming I chose to validate emails:
<strong>
Enter the Email: Jeremiah<br>
The Email, Jeremiah, is not correct! Please try again!<br>
Emails should follow this format: user@example.com or firstname.lastname@company.co.uk<br>

Enter the Email: j.emmanuel@alustudent.com<br>
The Email, j.emmanuel@alustudent.com, input is correct!<br>
Do you want to continue validating input [Y/N]: <br>
<strong>

When you enter a valid input, you will be asked if you want to continue to validate input.
If you select yes, the application will show you the start up menu. If you choose no, the application will close.
