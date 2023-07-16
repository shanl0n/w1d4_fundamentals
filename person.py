class Person:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.shopping_list = []

    def add_to_shopping(self, shopping_item):
        self.shopping_list.append(shopping_item)

    def remove_from_shopping(self, shopping_item):
        self.shopping_list.remove(shopping_item)
    
    # def print_shopping_list(self):
    #     return(self.shopping_list)
    
    def print_shopping_list(self):
        for products in self.shopping_list:
            print(products)


# Create a person class with the properties of  name (str), wallet (int). And a  shopping list (List) that starts off empty
# Write  methods to add and remove items from the shopping list
# Write a method called `print_shopping_list` to print out each item in the shopping list (using a loop)

# Task 5:
# Create an instance of the person class
# Add a string of “banana” to the shopping list of that person
# Add a string of “soap” to the shopping list of that person
# Print out the ‘name’ property of the person
# Call the person’s method to print out the shopping list.

