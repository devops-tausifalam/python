#Program 1: FirstName and its length
firstName = input("enter your first name: ")
print(firstName, ": length: ", len(firstName))

#Program 2: occurence of '$ in string
str1 = "India use INR-rupee system and America uses $ system, $1 = INR 80"
print("$occurence: ", str1.count("$"))

#Program 3: check if a number entered by user odd or even
oe_num = int(input("Please enter number: "))
if (oe_num != 0):
    divisibility = oe_num % 2
    if (divisibility == 0):
        print(oe_num, " is even.")
    else:
        print(oe_num, "is Odd.")
else:
    print(oe_num, " is even.")

#Program4: find the greatest of 3 numbers entered by the user.
greatest = float(input("Num1: ")) ,float(input("Num1: ")),float(input("Num1: "))
if (greatest[0] == greatest[1] and greatest[2] == greatest[1] and greatest[2] == greatest[0]):
    print("Looks like you're doing comedy!")
else: 
    print(max(greatest), " is greatest among ", greatest)

#Program5: if a number is a multiple of 7 or not.
multiple = float(input("Check divisibility of seven \n ENTER number: "))
if (multiple % 7 == 0):
    print(multiple, " is multiple of 7.")
else:
    print(multiple, " is not a multiple of 7.")
