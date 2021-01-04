#!/usr/bin/env python3
animals = ["dog", "cat", "lion", "bear", "wolf"]
for animal in animals:
    if (animal == animals[-1]):
        print(animal)
    else:
        print(animal, end=" ")
