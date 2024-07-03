import datetime as dt
import random
import smtplib
"""Use your own email following smtp protocol"""
MY_EMAIL = "mail@gmail.com"
PASSWORD = "password"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}")
    
    