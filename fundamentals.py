# Create a variable and assign it the value of “hello”
hello = "hello"
print(hello)
# Use an if statement to check if the variable is equal to hello, and if it is print”Hey there!”
if hello == "hello":
    print("Hey there!")
# Create a dictionary with the keys of “brand” with the value of “nike” and the key of “type” and the value of “shoe”.
test_dictionary = {"brand" :"nike", "type": "shoe"}
# Access and print out the value held under type from the dictionary just created
print(test_dictionary["type"])
# Task 2:
# Create a list of numbers from 1 to 10
list_of_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Using a loop add two to each number
new_list = []
for number in list_of_numbers:
    new_number = number + 2
    new_list.append(new_number)
# Using a loop print out each number in the list
for number in new_list:
    print(number)