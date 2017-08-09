#!/usr/bin/python3
import sys
import requests

from nousers import construct_unames, construct_passwords

default_url = "http://gjohnson3/pwd"

unames = construct_unames()
print("constructed {0} usernames for brute forcing...".format(len(unames)))

passwords = construct_passwords()
print("constructed {0} passwords for brute forcing...".format(len(passwords)))
prompt = "{0} web requests will be generated.  Do you want to continue?  (Y/n)  ".format(len(unames) * len(passwords))
result = input(prompt)
if not result == "Y": print('quitter!')

r = requests.get(default_url, auth=('admin', 'admin'))

if not r.status_code == 200:
    print("Exiting:  invalid url {0}").format(default_url)
    sys.exit(1)

print(r.content)
