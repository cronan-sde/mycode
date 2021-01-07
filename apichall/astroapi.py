#!/usr/bin/env python3

"""
    Author: Cody Cronberger
    gets data from api to print how many people are in space
    names of each person and craft they are on board

"""
#import request for accessing api
import requests

def main():
    req = requests.get("http://api.open-notify.org/astros.json")

    totalInSpace = req.json().get("number")
    print(f"People in space: {totalInSpace}")
    for num in range(0, totalInSpace):
        name = req.json().get("people")[num].get("name")
        craft = req.json().get("people")[num].get("craft")
        print(f"{name} is on the {craft}")

main()
