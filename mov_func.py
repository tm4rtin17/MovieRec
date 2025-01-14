#Import Modules
import pyinputplus as pyip
from mov_data import *
import sys

#Defines a function to retrieve each unique genre from the movie data matrix
def get_genres():
    return {index + 1: genre for index, genre in enumerate({movie[1] for movie in movie_matrix})}

#Define user input function
def select_genre():
    genres = get_genres() #Calls 'get_genres()' to store the dictionary in a variable

    #Prints a list of availble genres in a list format
    print("\f Select a Genre:")
    for key, value in genres.items():
        print(f"[{key}] {value}")

    #User selects genre based on availble genres within the data matrix
    user_genre = pyip.inputNum("\fWhat genre of movie were you thinking about watching? Enter the corresponding number\n", min=1, max=len(genres))
    return user_genre

#Sort through movies of the genre selected in a list format
def filter_by_genre(user_genre):
    genres = get_genres() #Calls 'get_genres()' to store the dictionary in a variable
    selected_genre = genres.get(user_genre, None) #The genre that the user selected is stored here as a numerical value

    #Values selected by the user that are not listed will return this error
    if not selected_genre:
        print("Invalid genre selected.")
        return
    
    #Message to user that the following movies belong to the genre that was selected
    print(f"\fHere is a list of {selected_genre.lower()} movies:\n")

    #List comprehension method to retrieve and print the list of movies of the selected genre from the data matrix, ratings are included in parenthesis
    for count, movie in enumerate([m for m in movie_matrix if m[1] == selected_genre], start=1):
        print(f"[{count}] {movie[0]} ({movie[2]}/10 stars)")
        movie_list.append(movie)

#Allows the user to select a movie and prints its description
def select_movie():
    mov = (pyip.inputNum("\fSelect the movie you are interested in...\n", min=0, max=3)) - 1   #User input to select a movie
    print(f'\f{movie_list[mov][0]}: ')  #Prints the movie name
    print(f'{movie_list[mov][3]}')      #Prints the movie description
    movie_list.clear()                  #Clears out the list so the user can search for more movies

def main():
    user_genre = select_genre()
    filter_by_genre(user_genre)
    select_movie()

    #Infinite loop allows user to search for a movie until they are done
    while True:
         nav_option = pyip.inputNum("\f [1] Go back\n [2] Select another genre\n [3] Exit Program\n", min=1, max=3)
         if nav_option == 1:
            filter_by_genre(user_genre)
            select_movie()
         elif nav_option == 2:
            break
         elif nav_option == 3:
             print("Enjoy your movie!")
             sys.exit()