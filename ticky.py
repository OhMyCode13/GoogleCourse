#!/usr/bin/env python3

import os
import re
import sys
import operator
import csv

error_counter = {}
error_user = {}
info_user = {}

#This function will read each line of the syslog.log file and check if it is an error or an info message.
def search_file():
    with open('syslog.log', "r") as my_file:
     for line in my_file:
        if " ERROR " in line:
            find_error(line)
            add_user_list(line, 1)
        elif " INFO " in line:
            add_user_list(line, 2)
    return


#If it is an error it will read the error from the line and increment into the dictionary
def find_error(str):
    match = re.search(r"(ERROR [\w \[]*) ", str)
    if match is not None:
        res = match.group(0).replace("ERROR ", "").strip()
        if res == "Ticket":
         res = "Ticket doesn't exist"
        if not res in error_counter:
            error_counter[res] = 1
        else:
            error_counter[res] += 1
    return

#This whill read the user from the string and add to the error or the info counter depending on the op number
def add_user_list(str, op):
    match = re.search(r'\(.*?\)', str)
    user = match.group(0)
    user_add = user.strip("()")
    if op == 1:
        if not user_add in error_user:
            error_user[user_add] = 1
        else:
            error_user[user_add] += 1
    elif op == 2:
        if not user_add in info_user:
            info_user[user_add] = 1
        else:
            info_user[user_add] += 1
    return

#This function will read the list, arrange it and return a tuple with the dictionary items
def sort_list(op, list):
    if op == "rev":
        ret = sorted(list.items(), key=operator.itemgetter(1), reverse=True)
    elif op == "fwd":
        ret = sorted(list.items(), key=operator.itemgetter(0))
    return ret

#This is an extra function which will read the value of a user in the error dictionary and return its value if key exists
def get_error_value(key_v):
    for key, value in error_user:
        if key is key_v:
            return value
    return 0

#This function writes both csv files
def write_csv(op):
    if op == "stat":
        with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csv_row = csv.DictWriter(output, fieldnames=fieldnames)
            csv_row.writeheader()
            for key, value in info_user:
                val_error = get_error_value(key)
                csv_row.writerow({'Username': key, 'INFO': value, 'ERROR': val_error})
    if op == "error":
        with open('error_message.csv', 'w', newline='') as output:
            fieldnames = ['Error', 'Count']
            csv_row = csv.DictWriter(output, fieldnames=fieldnames)
            csv_row.writeheader()
            for key, value in error_counter:
                csv_row.writerow({'Error': key, 'Count': value})
    return

#This function adds zero to the other dictionary in case that user is not a key, it will add a key with the user and value 0
def add_zeros():
    for user in error_user.keys():
        if user not in info_user:
            info_user[user] = 0
    for user in info_user.keys():
        if user not in error_user:
            error_user[user] = 0
    return


#This will execute the functions
search_file()
add_zeros()
error_counter = sort_list("rev", error_counter)
error_user = sort_list("fwd", error_user)
info_user = sort_list("fwd", info_user)
write_csv("stat")
write_csv("error")