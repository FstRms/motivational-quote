# Motivational Quote Email

Python script to send a random motivational quote via email.


### Prerequisites

- Python 3.9+
- [Poetry 0.12+](https://python-poetry.org/docs/#installation)
- A Gmail account
- Emails to recieve the quote.

#### Note
There are two versions of the script:

- motivational_quote.py
- monday_quote.py

They basically do the same, but 'monday_quote.py' verify if it is monday when you run it. It is build to run everyday on...let's say [pyhtonanywhere](https://www.pythonanywhere.com/)

#### Installing
- It is recommended to create a new [gmail account](https://accounts.google.com/signup).
- Make sure 2-Step Verification is off.
- Turn on ['Allow less secure apps'](https://myaccount.google.com/lesssecureapps). 
- Follow the variables in the .env.sample to a .env indicating your own email credentials.
- Add the receiver email accounts to 'email_list.txt' file(single line each).
- Open a terminal and navigate to project directory.
- Run poetry install.
- Run poetry shell.
- Run the command: 
    - python motivational_quote.py
- Check inbox for your motivational quote