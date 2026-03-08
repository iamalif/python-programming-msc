# Exercise 2: Movies

class Movie:

    # Declaring the mandatory initiator method
    def __init__(self, movie_id, title, genre, playing_time):
        # Storing all four attributes as private (as instructed) so they cannot be accessed or changed directly from outside the class.
        self.__id = movie_id
        self.__title = title
        self.__genre = genre
        self.__playing_time = playing_time

    # Declaring mutator or setter methods as instructed
    def set_id(self, movie_id):
        # Replacing the movie's current ID with a new one
        self.__id = movie_id

    def set_title(self, title):
        # Replacing the movie's current title with a new one
        self.__title = title

    def set_genre(self, genre):
        # Replacing the movie's current genre with a new one
        self.__genre = genre

    def set_playing_time(self, playing_time):
        # Replacing the movie's current playing time with a new value
        self.__playing_time = playing_time

    # Declaring accessor or getter methods as instructed
    def get_id(self):
        # Returning the movie's unique ID number
        return self.__id

    def get_title(self):
        # Returning the movie's title
        return self.__title

    def get_genre(self):
        # Returning the movie's genre (e.g. "Fantasy", "Comedy", "Drama", "Action")
        return self.__genre

    def get_playing_time(self):
        # Returning the movie's playing time (in minutes)
        return self.__playing_time


# Declaring functions for input validation
# Doing these validations using functions in order to keep the overall code reusable and clean

def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()  # Stripping whitespace to catch blank or space-only inputs

        # Rejecting completely empty inputs before going for conversion
        if not value:
            print("Input cannot be empty. Please try again.")
            continue

        try:
            number = int(value)  # Converting the string to an integer

            # Rejecting zero and negative numbers as IDs and durations must be at least 1
            if number <= 0:
                print("Please enter a number greater than zero.")
            else:
                return number  # Once valid input is received, exiting the loop and returning the value

        except ValueError:
            # This is when int() raised an error, which implies the input was not a whole number (e.g. "string" or "float")
            print(f"'{value}' is not a valid whole number. Please try again.")


def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()  # Stripping leading or trailing whitespaces

        if value:
            return value  # Once a non-empty string is received, returning it

        # Asking again if value is empty after stripping is done
        print("Input cannot be empty. Please try again.")


def get_menu_choice(prompt, valid_choices):
    while True:
        # Converting to lowercase before checking so that inputs like "Yes" or "YES" are treated the same as "yes"
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice  # Once a valid option is selected, returning it

        # Telling the user what went wrong and what the valid options are
        print(f"Invalid option '{choice}'. Please choose from: {', '.join(valid_choices)}.")


def id_is_unique(movies, movie_id):
    # Looping through all existing movies to check if any of them already has this ID
    for movie in movies:
        if movie.get_id() == movie_id:
            return False  # Implies match found, so this ID is already taken
    return True  # Implies no match found, so this ID is available


def find_movie_by_id(movies, movie_id):
    # Searching through the list for a movie whose ID matches the given one
    for movie in movies:
        if movie.get_id() == movie_id:
            return movie  # Returning the matching movie object
    return None  # Returning None to signal that no match was found


# Declaring named constants for each menu option as using constants avoids scattering raw numbers throughout the code - something that was directly taught in the class
ADD_MOVIE_CHOICE = 1
PRESENT_MOVIES_CHOICE = 2
UPDATE_MOVIE_CHOICE = 3
DELETE_MOVIE_CHOICE = 4
QUIT_CHOICE = 5


# Declaring the CRUD functions - one for each of the four main operations
def add_movie(movies):
    # Collecting all movie details and adding a new Movie object to the list
    print("\nAdd New Movie")

    # As the ID must be a positive integer and must not already be taken by another movie
    # Looping until the user provides an ID that passes both checks
    while True:
        movie_id = get_positive_int("Movie ID (unique number): ")
        if id_is_unique(movies, movie_id):
            break  # ID is valid and unique, so exiting the loop
        print(f"ID {movie_id} is already in use. Please choose a different ID.")

    title = get_non_empty_string("Title: ")
    genre = get_non_empty_string("Genre (e.g. Fantasy, Comedy, Drama, Action): ")
    playing_time = get_positive_int("Playing time (minutes): ")

    # Creating a new Movie object with the collected data and appending it to the list
    movie = Movie(movie_id, title, genre, playing_time)
    movies.append(movie)
    print(f"Movie '{title}' added successfully.")


def present_movies(movies):
    # Printing all movies currently stored in the list
    print("\nAll Movies")

    # Checking if the list is empty before trying to display anything
    if not movies:
        print("No movies registered yet.")
        return

    # Printing a formatted header row so the output is easy to read
    print(f"{'ID':<6} {'Title':<30} {'Genre':<15} {'Time (min)'}")
    print("-" * 60)  # Adding separator line aligned with the header

    # Looping through every movie and printing its details in aligned columns
    for movie in movies:
        print(
            f"{movie.get_id():<6} "
            f"{movie.get_title():<30} "
            f"{movie.get_genre():<15} "
            f"{movie.get_playing_time()}"
        )


def update_movie(movies):
    # Finding an existing movie by ID and changing one or more of its fields
    print("\nUpdate Movie")

    # Checking if the list is empty before trying to update anything
    if not movies:
        print("No movies registered yet.")
        return

    # Looking up the movie the user wants to edit
    movie_id = get_positive_int("Enter the ID of the movie to update: ")
    movie = find_movie_by_id(movies, movie_id)

    # If find_movie_by_id returned None, that ID does not exist in the list
    if movie is None:
        print(f"No movie with ID {movie_id} was found.")
        return

    # Showing the current values so the user knows what they are about to change
    print(f"\nCurrent details - ID: {movie.get_id()} | Title: {movie.get_title()} | "
          f"Genre: {movie.get_genre()} | Time: {movie.get_playing_time()} min")

    # Presenting a sub-menu so the user can choose which field(s) to update
    print("\nWhat would you like to update?")
    print("1. Title")
    print("2. Genre")
    print("3. Playing time")
    print("4. All fields")
    field_choice = get_menu_choice("Enter choice (1-4): ", ["1", "2", "3", "4"])

    # Using individual if-statements so that option 4 triggers all three blocks
    if field_choice in ("1", "4"):
        new_title = get_non_empty_string("New title: ")
        movie.set_title(new_title)  # Calling the setter method to update the private attribute

    if field_choice in ("2", "4"):
        new_genre = get_non_empty_string("New genre: ")
        movie.set_genre(new_genre)  # Calling the setter method to update the private attribute

    if field_choice in ("3", "4"):
        new_time = get_positive_int("New playing time (minutes): ")
        movie.set_playing_time(new_time)  # Calling the setter method to update the private attribute

    print(f"Movie ID {movie_id} updated successfully.")


def delete_movie(movies):
    # Finding a movie by ID and removing it from the list after confirmation
    print("\nDelete Movie")

    # Checking if the list is empty before trying to delete anything
    if not movies:
        print("No movies registered yet.")
        return

    # Looking up the movie the user wants to remove
    movie_id = get_positive_int("Enter the ID of the movie to delete: ")
    movie = find_movie_by_id(movies, movie_id)

    # If find_movie_by_id returned None, that ID does not exist in the list
    if movie is None:
        print(f"No movie with ID {movie_id} was found.")
        return

    # Showing what was found and asking the user to confirm before permanently removing it
    print(f"Found: '{movie.get_title()}' (ID {movie.get_id()})")
    confirm = get_menu_choice("Are you sure you want to delete it? (yes/no): ", ["yes", "no"])

    if confirm == "yes":
        movies.remove(movie)  # Removing the actual object from the list
        print(f"Movie '{movie.get_title()}' deleted successfully.")
    else:
        # User chose "no", so cancelling without making any changes
        print("Delete cancelled.")


# Declaring a dedicated function to display the menu, taking inpiration from the geometry.py file as mentioned in the instructions
def display_menu():
    # Printing each option on its own line so the menu is easy to read
    print("\nMovie Manager")
    print(f"{ADD_MOVIE_CHOICE}. Add movie")
    print(f"{PRESENT_MOVIES_CHOICE}. Present all movies")
    print(f"{UPDATE_MOVIE_CHOICE}. Update movie")
    print(f"{DELETE_MOVIE_CHOICE}. Delete movie")
    print(f"{QUIT_CHOICE}. Quit")
    print()


# Following is the main program
def main():
    movies = []  # This list will be holding all Movie objects created during the session

    # Building the list of valid choices from the constants so it stays in sync automatically
    menu_options = [str(ADD_MOVIE_CHOICE), str(PRESENT_MOVIES_CHOICE),
                    str(UPDATE_MOVIE_CHOICE), str(DELETE_MOVIE_CHOICE), str(QUIT_CHOICE)]

    # Keeping the menu running in an infinite loop until the user explicitly chooses to quit
    while True:
        display_menu()  # Calling the dedicated display function, as shown in the geometry.py example

        choice = get_menu_choice("Select an option (1-5): ", menu_options)

        # Routing the user's choice to the appropriate CRUD function using the named constants
        if choice == str(ADD_MOVIE_CHOICE):
            add_movie(movies)
        elif choice == str(PRESENT_MOVIES_CHOICE):
            present_movies(movies)
        elif choice == str(UPDATE_MOVIE_CHOICE):
            update_movie(movies)
        elif choice == str(DELETE_MOVIE_CHOICE):
            delete_movie(movies)
        elif choice == str(QUIT_CHOICE):
            print("Goodbye!")
            break  # Exiting the while loop, which ends the program


main()
