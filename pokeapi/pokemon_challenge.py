#!/usr/bin/env python3

"""
    Author: Cody Cronberger
    Allows users to get data on a pokemon of their choice by utilizing
    Pokemon API

"""

#import requests to easily access api
import requests

def main():
    pokeapi = getPokemon("https://pokeapi.co/api/v2/pokemon/")
    formsDataUrl = requests.get(f"{pokeapi.get('forms')[0].get('url')}").json()
    name = pokeapi.get('forms')[0].get('name')

    frontImage = formsDataUrl.get("sprites").get("front_default")
    howManyGames = len(pokeapi.get("game_indices"))

    moves = []
    for move in pokeapi.get("moves"):
        moves.append(move.get("move").get("name"))
    
    #save image to file
    savePokemonImg(name, frontImage)
    #send data to display function
    displayPokemon(name, frontImage, howManyGames, moves)


#function to get user input and return pokemon of their choice
def getPokemon(url):
    req = None
    while True:
        print("Which pokemon would you like info on?\nEnter either name or number of pokemon if known: ")
        pokemon = input(">> ").strip().lower()
        try:
            req = requests.get(url + pokemon).json()
            break
        except:
            print("Could not find pokemon by that name, try again")
    return req


#display output
def displayPokemon(name, imgUrl, gameCount, moves):
    print(f"Pokemon -- {name}\n")
    print(f"View image of {name} at {imgUrl} or check the newly created {name}.png file\n")
    print(f"{name} appeared in {gameCount} games\n\nCheck out {name}'s list of moves here:")
    for move in moves:
        if move == moves[-1]:
            print(move)
        else:
            print(move, end=",")
                

#save image to file
#req.content returns response content in bytes
#wb argument means write in binary mode so we can write the image
def savePokemonImg(name, imgUrl):
    req = requests.get(imgUrl)
    with open(f"/home/student/static/{name}.png", "wb") as f:
        f.write(req.content)


#If ran directly run the main method
if __name__ == "__main__":
    main()
