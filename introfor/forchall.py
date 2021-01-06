#!/usr/bin/env python3

count = 5
for i in range(count):
    for j in range(i):
        print("*", end=" ")
    print("")

for i in range(count, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print("")
