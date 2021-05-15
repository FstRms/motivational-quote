"""Script to send motivational quotes via email on Mondays"""

import os
import sys
import smtplib
import datetime as dt
import random
from dotenv import load_dotenv

load_dotenv()
ORIGIN_EMAIL = os.environ.get("ORIGIN_EMAIL")
MY_PASSW = os.environ.get("EMAIL_PASSWORD")

with open("email_list.txt", "r") as emails:
    receivers = emails.readlines()
if len(receivers) == 1:
    receivers = receivers[0]
elif len(receivers) == 0:
    print("Destination emails were not provided")
    sys.exit()
else:
    receivers = [email.strip() for email in receivers]

with open("quotes.txt", "r") as q_file:
    quotes = q_file.readlines()

check_today = dt.datetime.now()
your_quote = "Subject:Your Motivational Quote\n\n" + random.choice(quotes)

if check_today.weekday() == 0:
    print("Today is Monday")
    # print(your_quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=ORIGIN_EMAIL, password=MY_PASSW)
        connection.sendmail(
            from_addr=ORIGIN_EMAIL, to_addrs=receivers, msg=your_quote.encode("utf-8")
        )
