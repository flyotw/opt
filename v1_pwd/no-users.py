#!/usr/bin/python3

from constants import alphabet

files = [
    "../wordlists/SecLists/Usernames/Names/top_1000_usa_familynames_english.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_femalenames_english.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_malenames_english.txt",
]

raw_names = list(map((lambda file : open(file, "r").read().splitlines()), files))

def construct_uname(prepended_chars, raw_name, is_uppercase):
    raw_username = prepended_chars + raw_name
    return raw_username.upper() if is_uppercase else raw_username.lower()

map(construct_uname, alphabet, True)



