#!/usr/bin/env python3
user = input("What is your name?").strip()
icecream = ["flavors", "salty"]
icecream.append(99)

print(f"{icecream[-1]} {icecream[0]}, and {user} chooses to be {icecream[1]}.")
