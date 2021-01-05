#!/usr/bin/env python3

#dic to hold movie titles as keys and synopsis as the value
movies = {"Die Hard": "An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza in Los Angeles",
        "Monty Python and the Holy Grail": "King Arthur and his Knights of the Round Table embark on a surreal, low-budget search for the Holy Grail, encountering many, very silly obstacles",
        "Billy Madison": "In order to inherit his fed up father's hotel empire, an immature and lazy man must repeat grades 1-12 all over again",
        "Predator": "A team of commandos on a mission in a Central American jungle find themselves hunted by an extraterrestrial warrior",
        "Commando": "A retired Special Forces colonel tries to save his daughter, who was abducted by his former subordinate",
        "Jeremiah Johnson": "Mountain man who wishes to live the life of a hermit becomes the unwilling object of a long vendetta by the Crow tribe and proves to be a match for their warriors in single combat on the early frontier",
        "Spaceballs": "A star pilot and his sidekick must come to the rescue of a Princess and save the galaxy from a ruthless race of beings known as Spaceballs"}

#create a list to index movie titles
movieList = []
for movie in movies:
    movieList.append(movie)

#prints the list of movie titles in dic with a numerical value as a key
#allows users to choose a movie from the list and get the synopsis for the movie back
#only allows real numbers and numbers that are within the list
def choose_movie():
    #print movies in movie list
    for movie in movieList:
        print(f"{movieList.index(movie)}:{movie}")

    #prompt user to choose a movie from list
    user_choice = -1
    isValid = False
    while not isValid:
        try:
            user_choice = int(input("Enter the number associated with the movie you'd like to see synopsis of: "))
            if user_choice < 0 or user_choice >= len(movieList):
                print(f"Please choose a number associated with a movie {user_choice} is outside the range of movies")
            else:
                isValid = True
        except:
            print("You must enter a valid number")


    #return the synopsis of that movie
    user_movie = movieList[user_choice]
    print(f"\n{user_movie} Synopsis -\n{movies[user_movie]}.\n")
    #calls choose_again function to allow users to continue looking up movie synopsis
    choose_again()

#Ask if user would like to choose another movie or exit
def choose_again():
    while True:
        user_choice = input("Would you like to choose another movie? y/n: ")
        if user_choice.lower() == "y":
            choose_movie()
            break
        elif user_choice.lower() == "n":
            break
        else:
            print("Please type either y or n")

#run choose_movie
choose_movie()

#exit program
print("\nExiting the program")
