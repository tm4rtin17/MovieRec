#Import Modules
import pyinputplus as pyip
from mov_data import *
from mov_func import *

#Initial run of the main function
main()

#Infinite loop to allow user to search an indefinite amount of times until ready to quit
while True:
    rerun = pyip.inputYesNo('\fWould you like to look for another movie? (y/n)\n')
    if rerun is 'yes':
        main()
    else:
        print('\fEnjoy your movie!') #no answer ends the program
        break
