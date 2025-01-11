#Import Modules
import pyinputplus as pyip
from mov_data import *

#Define user input function
def select_genre():
    user_genre = pyip.inputNum("What genre of movie were you thinking about watching? Enter the corresponding number\n [1] Horror, [2] Comedy, [3] Action\n", min=1, max=3)
    return user_genre

#Sort through movies of the genre selected in a list format
def filter_by_genre(user_genre):
    genres = {1: "Horror", 2: "Comedy", 3: "Action"} #Dictionary to define genres and map to their number
    movie_list.clear()

    if user_genre in genres:
        selected_genre = genres[user_genre]
        print(f"\nHere is a list of {selected_genre.lower()} movies:\n")
        for count, movie in enumerate([m for m in movie_matrix if m[1] == selected_genre], start=1):
            print(f'{count}. {movie[0]} ({movie[2]}/10 stars)')
            movie_list.append(movie)
    else:
        print("Invalid genre selection.")

#Allows the user to select a movie and prints its description
def select_movie():
    mov = (pyip.inputNum("\fEnter the corresponding number of the movie you are interested in...\n", min=0, max=3)) - 1   #User input to select a movie
    print(f'\f{movie_list[mov][0]}: ')  #Prints the movie name
    print(f'{movie_list[mov][3]}')      #Prints the movie description
    movie_list.clear()                  #Clears out the list so the user can search for more movies

def main():
    user_genre = select_genre()
    filter_by_genre(user_genre)
    select_movie()
