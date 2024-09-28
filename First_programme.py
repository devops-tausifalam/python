#Program 1: It is about simple division of float numbers and returning their type using tupl
num1 = 8958937768937
num2 = 2851718461558

# Use a list comprehension to get the types of all variables in one call
types = [type(x) for x in (num1, num2, 42)]

print(types)  # This will print the types of num1, num2, and 42
print(float(num1 / num2))  # Perform and print the division as a float

#Program 2: this program returns number of char in the first variable with/without spaces
# I prefilled this variable for you, you don't need to touch it.

whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."

# Enter your code below:
n_char = len(whetting_your_appetite)

#A len() function can measure the length of lists,strings ... nearly everything

print(n_char)

#excluding spaces to get actual letter count
n_char_2 = len(whetting_your_appetite.replace(" ",""))
print(n_char_2, ", Number of spaces in particular: ", (n_char - n_char_2))

#Program 3: using for loop and showing squares of first 10 whole numbers
first_sqNum = [0,1,2,3,4,5,6,7,8,9]

for loop in first_sqNum:
    print("Squared Num: ", loop**2)
    #later-on I would like to do something like: print("square of 0 is:") till 9 like this