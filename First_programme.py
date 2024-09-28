#Program 1
num1 = 8958937768937
num2 = 2851718461558

# Use a list comprehension to get the types of all variables in one call
types = [type(x) for x in (num1, num2, 42)]

print(types)  # This will print the types of num1, num2, and 42
print(float(num1 / num2))  # Perform and print the division as a float
