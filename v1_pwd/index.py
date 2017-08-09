#!/usr/bin/python3

from nousers import construct_unames, construct_passwords

unames = construct_unames()
print("constructed {0} usernames for brute forcing...".format(len(unames)))

passwords = construct_passwords()
print("constructed {0} passwords for brute forcing...".format(len(passwords)))
prompt = "{0} web requests will be generated.  Do you want to continue?  (Y/n)".format(len(unames) * len(passwords))
result = input(prompt)
print(result)