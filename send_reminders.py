#!/usr/bin/env python3

import csv
import datetime
import email
import smtplib
import sys

# This script is 90% there. Missing the last part, which I believe is the main system call section.
# Stay tuned, though this may not be a script that is usable since I haven't seen it associated with any 
# open source license. May just be one for me to use privately/testing/not for profit. 

def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("     send_reminders 'date|Meeting Title|emails' ")
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(date, title, name):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi {name}!

This is a quick email to remind you all that we have a meeting about:
 "{title}"
the {weekday} {date}.

See you there.
''')
    return message

def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names[row[0]] == row[1]
    return names

def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP('localhost')
    names = read_names(contacts)
    for email in emails.split(','):
        name = names[email]
        message = message_template(date, title, name)
        message['From'] = 'noreply@Art4.Tech'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
