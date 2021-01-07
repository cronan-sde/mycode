#!/usr/bin/env python3

import netifaces

def getUserDevice():
    device = input("Enter adapter name to find IP for: ").strip()

    print("\n***** details of interface - " + device + " *****")
    try:
        print("IP: ", end="")
        print(netifaces.ifaddresses(device)[netifaces.AF_INET][0]['addr'])
    except:
        print("Could not collect adapter information")


if __name__ == "__main__":
    getUserDevice()
    print("Exiting the program")
