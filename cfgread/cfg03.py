#!/usr/bin/env python3

#get file from user
user_file = input("input file name: ").strip()

## create file object in "r"ead mode
with open(user_file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(len(configlist))
