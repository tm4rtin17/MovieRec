#Import Modules
import pyinputplus as pyip

#Define movie data
movie_matrix = [['Friday the 13th', 'Horror', 8, 'A group of teenage camp counselors attempt to re-open an abandoned summer camp with a tragic past, but they are stalked by a mysterious, relentless killer.'],
                ['Nightmate on Elm Street', 'Horror', 7, 'Several midwestern teenagers fall prey to Freddy Krueger, a disfigured midnight mangler who preys on the teenagers in their dreams -- which, in turn, kills them in reality'],
                ['Alien', 'Horror', 9, 'After investigating a mysterious transmission of unknown origin, the crew of a commercial spacecraft encounters a deadly lifeform.'],
                ['Happy Gilmore', 'Comedy', 7, 'A Hockey player wannabe finds out that he has the most powerful golf drive in history. He joins the P.G.A. tour to make some money to save grandmas house.'],
                ['Billy Madison', 'Comedy', 6, 'In order to inherit his fed-up father Brians hotel empire, immature and lazy Billy Madison must repeat grades one through twelve all over again.'],
                ['Goon', 'Comedy', 8, 'Labeled an outcast by his brainy family, a bouncer overcomes long odds to lead a team of under performing misfits to semi-pro hockey glory, beating the crap out of everything that stands in his way.'],
                 ['The Fast and the Furious', 'Action', 7, 'Los Angeles police officer Brian OConner must decide where his loyalty really lies when he becomes enamored with the street racing world he has been sent undercover to end it.'],
                 ['National Treasure', 'Action', 7, 'A historian races to find the legendary Templar Treasure before a team of mercenaries.'],
                 ['The Dark Knight', 'Action', 9, 'When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.']]


#Define user input function
def select_genre():
    print('[1] Horror, [2] Comedy, [3] Action')
    user_genre = pyip.inputNum("What genre of movie were you thinking about watching? Enter the corresponding number", min=1, max=3)
    return user_genre

#Sort through movies of the genre selected in a list format
def sort_genre(user_genre):
    
    count = 1       #Counter to define numbered list in print statement
    print('')       #Prints blank space for clean formatting

    if user_genre == 1: 
        print("Here is a list of horror movies: ")
        for movie in movie_matrix:
            if movie[1] == 'Horror':
                print(f'{count}.{movie[0]} ({movie[2]}/10 stars)')
                movie_list.append(movie)
                count += 1
    elif user_genre == 2:
        for movie in movie_matrix:
            if movie[1] == 'Comedy':
                print(f'{count}.{movie[0]} ({movie[2]}/10 stars)')
                movie_list.append(movie)
                count += 1
    elif user_genre == 3:
        for movie in movie_matrix:
            if movie[1] == 'Action':
                print(f'{count}.{movie[0]} ({movie[2]}/10 stars)')
                movie_list.append(movie)
                count += 1

#Allows the user to select a movie and prints its description
def select_movie():
    print('')       #Blank print statement for formatting only
    mov = (pyip.inputNum("Enter the corresponding number of the movie you are interested in...", min=0, max=3)) - 1   #User input to select a movie
    print('')                           #Prints blank space for formatting cleanliness
    print(f'{movie_list[mov][0]}: ')    #Prints the movie name
    print(f'{movie_list[mov][3]}')      #Prints the movie description
    movie_list.clear()                  #Clears out the list so the user can search for more movies

#Main Program
movie_list = [] #Movies append after genre sorting

user_genre = select_genre()
sort_genre(user_genre)
select_movie()

while True:
    rerun = pyip.inputYesNo('Would you like to look for another movie? (y/n)')
    if rerun is 'yes':
        print('')       #Blank space for formatting only
        
        #Functions rerun infinitely as desired
        user_genre = select_genre()
        sort_genre(user_genre)
        select_movie()
    else:
        print('')       #Blank space for formatting only
        print('Enjoy your movie!')
        break
