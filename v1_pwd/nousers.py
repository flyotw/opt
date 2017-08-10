#!/usr/bin/python3
import utils
from constants import alphabet

lastname_files = [
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_familynames_english.txt",
]

name_files = [
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_femalenames_english.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_malenames_english.txt",
    "../wordlists/SecLists/Usernames/top_shortlist.txt"
]

password_files = [
    #"../wordlists/SecLists/Passwords/10_million_password_list_top_1000.txt",
    "../wordlists/SecLists/Passwords/rockyou-5.txt"
]

raw_last_names = utils.read_files_to_list(lastname_files)
raw_names = utils.read_files_to_list(name_files)
passwords = utils.read_files_to_list(password_files)

def construct_uname(prepended_char, raw_name, is_uppercase):
    raw_username = prepended_char + raw_name
    return raw_username.upper() if is_uppercase else raw_username.lower()

def construct_unames():
    val = []
    if not len(raw_last_names) == 0: #build first letter of first name, whole last name set
        for char in alphabet:
            for name in raw_last_names:
               val.append(construct_uname(char, name, False))
    for name in raw_names:
        val.append(name)
    return val

def construct_passwords():
    return passwords