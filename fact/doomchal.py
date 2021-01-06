#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
#Hey Not Too Rough
#loop that returns animals from NE farm
def notTooRough():
    for farm in farms:
        if farm["name"] == "NE Farm":
            animals = farm["agriculture"]
            for animal in animals:
                print(animal)


#Hurt Me Plenty
#ask user to choose a farm, return plants/animals raised on that farm
def hurtMePlenty():
    farmName = ""
    while True:
        user_choice = input("Choose a farm type (NE, W, or SE): ").strip().upper()
    
        if user_choice == "NE":
            farmName = "NE Farm"
            break
        elif user_choice == "W":
            farmName = "W Farm"
            break
        elif user_choice == "SE":
            farmName = "SE Farm"
            break
        else:
            print("Please choose a valid farm")

    for farm in farms:
        if farm["name"] == farmName:
            for agr in farm["agriculture"]:
                print(agr)


#NIGHTMARE
#Ask user for farm, only return Animals from that farm
def nightmare():
    farmName = ""
    while True:
        user_choice = input("Choose a farm type (NE, W, or SE): ").strip().upper()

        if user_choice == "NE":
            farmName = "NE Farm"
            break
        elif user_choice == "W":
            farmName = "W Farm"
            break
        elif user_choice == "SE":
            farmName = "SE Farm"
            break
        else:
            print("Please choose a valid farm")

    for farm in farms:
        if farm["name"] == farmName:
            for animal in farm["agriculture"]:
                if animal in animals:
                    print(animal)

nightmare()
