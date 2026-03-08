# Exercise 1: Animals

class Pet:

    # Declaring the mandatory initiator method
    def __init__(self, name, animal_type, age):
        # Storing all three attributes as private (as instructed) so they cannot be accessed or changed directly from outside the class.
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Declaring mutator or setter methods as instructed
    def set_name(self, name):
        # Replacing the pet's current name with a new one
        self.__name = name

    def set_animal_type(self, animal_type):
        # Replacing the pet's current animal type with a new one
        self.__animal_type = animal_type

    def set_age(self, age):
        # Replacing the pet's current age with a new value
        self.__age = age

    # Declaring accessor or getter methods as instructed
    def get_name(self):
        # Returning the pet's name
        return self.__name

    def get_animal_type(self):
        # Returning the type of animal (e.g. "Dog", "Cat", "Bird")
        return self.__animal_type

    def get_age(self):
        # Returning the pet's age (in years)
        return self.__age


# Declaring functions for input validations
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

            # Rejecting zero and negative numbers as age and pet count must be at least 1
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
            return value  # Once non-empty string is received, returning it

        # Asking again if value is empty after stripping is done
        print("Input cannot be empty. Please try again.")


def get_menu_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()

        if choice in valid_choices:
            return choice  # Once valid option is selected, returning it

        # Telling the user what went wrong and what the valid options are
        print(f"Invalid choice '{choice}'. Please enter one of: {', '.join(valid_choices)}.")


# Following is the main program
def main():
    pets = []  # This list will be holding all Pet objects created during the session

    # Asking how many pets the user wants to register before starting the entry loop
    num_pets = get_positive_int("How many pets do you want to enter? ")

    # Using a counter-controlled while loop to collect data for each pet, one at a time
    count = 0
    while count < num_pets:
        print(f"\nEnter details for pet {count + 1}")

        # Collecting each field individually, with validation on every input
        # This is where I reap the joy of writing all that code earlier for validations and is perhaps the biggest technical implementation I have done in this overall program
        name = get_non_empty_string("Pet name: ")
        animal_type = get_non_empty_string("Animal type (e.g. Dog, Cat, Bird): ")
        age = get_positive_int("Age: ")

        # Creating a new Pet object with the collected data and adding it to the list
        pet = Pet(name, animal_type, age)
        pets.append(pet)

        count += 1  # Incrementing the counter to move to the next pet while also ensuring the while loop doesn't go on infinitely

    # Once all pets are entered, asking the user how they want to view the results
    print("\nHow would you like to display the pets?")
    print("1. Show all pets")
    print("2. Show all pets of a certain type")
    choice = get_menu_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        # Option 1: Looping through every pet in the list and printing the details
        print("\nAll Pets")
        for pet in pets:
            print(f"Name: {pet.get_name()}, Type: {pet.get_animal_type()}, Age: {pet.get_age()}")

    else:
        # Option 2: Asking for a type to filter by, and then only showing the matching pets
        # Converting the filter input to lowercase so the comparison is not case sensitive
        filter_type = get_non_empty_string("Enter the animal type to filter by: ").lower()
        print(f"\nPets of type '{filter_type.capitalize()}'")

        found = False  # Tracking whether at least one matching pet was found
        for pet in pets:
            # Comparing both sides in lowercase to ensure case sensitivity is addressed
            if pet.get_animal_type().lower() == filter_type:
                print(f"Name: {pet.get_name()}, Type: {pet.get_animal_type()}, Age: {pet.get_age()}")
                found = True

        # If no pets matched the requested type, informing the user clearly
        if not found:
            print(f"No pets of type '{filter_type.capitalize()}' were found.")


main()
