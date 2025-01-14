# MovieRec (v1.1.1)

## Overview
MovieRec is a Python-based program that allows users to explore a curated list of movies by genre and select a movie to view its description. Users can continue browsing until they find the perfect movie to watch.

## Features
- Browse movies by genre.
- View movie ratings and descriptions.
- Search for additional movies as desired.
    - [**New**]: User can now go back a page to the list of movies in the selected genre instead of having to re-select the genre each time.
- Simple and interactive user input.

## Installation
### Prerequisites
- Python 3.13.1
- Install the `pyinputplus` module:
  ```bash
  pip install pyinputplus
  ```

### Steps
1. Clone or download the project repository.
2. Save the script file in your desired directory.
3. Ensure Python 3.13.1 is installed on your system.

## Usage
1. Run the script in your Python environment:
   ```bash
   python movie_selector.py
   ```
2. Follow the prompts to select a genre and choose a movie from the list.
3. Continue browsing or exit when satisfied.

### Example Interaction
```text
[1] Horror
[2] Action
[3] Comedy
What genre of movie were you thinking about watching? Enter the corresponding number: 1

Here is a list of horror movies:
[1] Friday the 13th (8/10 stars)
[2] Nightmare on Elm Street (7/10 stars)
[3] Alien (9/10 stars)

Enter the corresponding number of the movie you are interested in: 2

Nightmare on Elm Street:
Several midwestern teenagers fall prey to Freddy Krueger, a disfigured midnight mangler who preys on the teenagers in their dreams -- which, in turn, kills them in reality.

[1] Go back
[2] Select another genre
[3] Exit Program

Enjoy your movie!
```

## File Structure
- `main.py`: The main Python script for the program.
- `mov_func.py`: Contains all of the functions for the main program.
- `mov_data.py`: Contains all of the data for the program.

## Possible Future Improvements
- Minor:
  - Add logic to automatically sort generes and movie titles alphabetically (A-Z).
  - Allow the user to select an option to sort movies by rating and back to alphabetically if desired.
- Major:
  - Increase dataset by webscraping movie data with IMDB API.
  - Add data to the datamatrix to store information of what streaming services a movie can be watched on.
  - Limit selection to 10 different genres/movies at a time for clean output of data to console. 

## Changelog (v1.1.1)
- Removed infinite loop from 'main.py' and nested it within the `main()` function.
- Created new logic inside infinite loop to allow the user to move back a page to see the list of movies of the selected genre.
- Various clerical adjustments made to print statements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Movie descriptions are for demonstration purposes only and may not be verbatim from official sources.

Enjoy exploring movies and finding the perfect one to watch!

