from person import *

person1 = Person("Sean", 10)  # creates a new Student object

person1.add_to_shopping("soap")
person1.add_to_shopping("banana")

print(f"{person1.name} is going shopping and has {person1.wallet} pounds in his wallet.")

print(f"The items in his shopping list are: {person1.print_shopping_list()}")

# Create a person class with the properties of  name (str), wallet (int). And a  shopping list (List) that starts off empty
# Write  methods to add and remove items from the shopping list
# Write a method called `print_shopping_list` to print out each item in the shopping list (using a loop)

# Task 5:
# Create an instance of the person class
# Add a string of “banana” to the shopping list of that person
# Add a string of “soap” to the shopping list of that person
# Print out the ‘name’ property of the person
# Call the person’s method to print out the shopping list.