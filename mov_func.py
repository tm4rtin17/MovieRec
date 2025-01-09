#Import Modules
import pyinputplus as pyip
from mov_data import *

#Define user input function
def select_genre():
    print('\f[1] Horror, [2] Comedy, [3] Action')
    user_genre = pyip.inputNum("What genre of movie were you thinking about watching? Enter the corresponding number\n", min=1, max=3)
    return user_genre

#Sort through movies of the genre selected in a list format
def sort_genre(user_genre):
    count = 1  #Counter to define numbered list in print statement
    if user_genre == 1: 
        print("\fHere is a list of horror movies: \n")
        for movie in movie_matrix:
            if movie[1] == 'Horror':
                print(f'{count}.{movie[0]} ({movie[2]}/10 stars)')
                movie_list.append(movie)
                count += 1
    elif user_genre == 2:
        print("\fHere is a list of comedy movies: \n")
        for movie in movie_matrix:
            if movie[1] == 'Comedy':
                print(f'{count}.{movie[0]} ({movie[2]}/10 stars)')
                movie_list.append(movie)
                count += 1
    elif user_genre == 3:
        print("\fHere is a list of horror movies: \n")
        for movie in movie_matrix:
            if movie[1] == 'Action':
                print(f'{count}.{movie[0]} ({movie[2]}/10 stars)')
                movie_list.append(movie)
                count += 1

#Allows the user to select a movie and prints its description
def select_movie():
    mov = (pyip.inputNum("\fEnter the corresponding number of the movie you are interested in...\n", min=0, max=3)) - 1   #User input to select a movie
    print(f'\f{movie_list[mov][0]}: ')  #Prints the movie name
    print(f'{movie_list[mov][3]}')      #Prints the movie description
    movie_list.clear()                  #Clears out the list so the user can search for more movies

def main():
    user_genre = select_genre()
    sort_genre(user_genre)
    select_movie()
