"""
PetMatch is a program that helps users find the perfect pet for their lifestyle.

Created by: Wyspwo
"""

# defines the function that will be used later on to recommend a pet based on the user's inputs
def recommend_pet(features):
    # inputs the user's features into variables to be used in the if statements used to detemine the best pet for the user
    allergies = features["allergies"] 
    time = features["time"]
    space = features["space"]
    budget = features["budget"]
    noise = features["noise"]

    # determines the user's pets from the choices
    if allergies == "yes":
        return "Fish", "Because you have allergies, a fish may be a better fit." 
        # 2 statements are used to return the pet and the reason for that pet

    # if no then move on to the next if statement, etc.

    elif time >= 2 and space == "yard":
        return "Dog", "Because you have 2+ hours a day and a yard, a dog could fit your lifestyle."

    elif time < 1 or noise == "low":
        return "Fish", "Because you have limited time and/or low noise tolerance, fish may be a better choice."

    elif budget == "low":
        return "Small mammal", "Because you have a lower budget, a small mammal may be a better fit."

    else:
        return "Cat", "Because your answers fit a lower-maintenance pet, a cat could be a good choice."

# function used to make sure the user inputs a valid response for yes or no questions
def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower() # gets the user's input

        if answer == "yes" or answer == "no":
            return answer

        print("Please enter yes or no.")

# function used to make sure the user inputs a valid response for number questions
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt)) # gets the user's input

            if number >= 0:
                return number

            print("Please enter a number 0 or higher.")

        except ValueError: # warns the user if they don't input a number
            print("Please enter a valid number.")

# function used to make sure the user inputs a valid response for multiple choice questions
def get_choice(prompt, choices):
    while True:
        answer = input(prompt).lower() # gets the user's input

        if answer in choices:
            return answer

        print("Choose from:", ", ".join(choices)) # lists the valid choices for the user to choose from


# weclomes the user to the program and explains what it is
print("Welcome to PetMatch!")
print("Answer a few questions to find a pet that fits you.\n")

# gets the user's inputs for the questionnaire
allergies = get_yes_no("Do you have allergies? (yes/no): ")
time = get_number("How many hours per day can you spend with a pet? ")
space = get_choice("Do you live in an apartment or house with a yard? ", ["apartment", "yard"])
budget = get_choice("What is your budget? (low/medium/high): ", ["low", "medium", "high"])
noise = get_choice("What is your noise tolerance? (low/medium/high): ", ["low", "medium", "high"])

# turns the user's inputs into a dictionary
features = {
    "allergies": allergies,
    "time": time,
    "space": space,
    "budget": budget,
    "noise": noise
}

# uses the first established function to recommend a pet based on the user's inputs
# 2 variables in one because the function returns 2 values, the pet and the reason for that pet
pet, reason = recommend_pet(features)
print() # new line for spacing

# prints the recommended pet and the reason for that recommendation
print("PetMatch Recommendation:")
print("Recommended pet:", pet)
print(reason)
print() # new line for spacing
print("Thank you for using PetMatch! We hope you have found the perfect pet!")