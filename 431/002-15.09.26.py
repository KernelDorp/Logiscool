#Task 1 - Return the length of the text
print(input("Give me a string and I will tell you the length in characters (including spaces) : ").__len__())
#We use __len__ for measuring the length of the string (characters)

#Task 2 - Split the string at the specified character
print(input("Give me a string to split apart at every whitespace : ").split(" "))
print(input("Give me a string to split apart at every letter a: ").split("a"))
#We use split() to split strings at a specific character

#Task 3 - Count how many times a character appears in a string
print(input("Give me a string to count how many times there appear whitespaces in your string: ").count(" "))
#Counting starts from 0

#Task 4 - Find a specific character or string in the given string
print(input("Give me a string to find Nemo in it ;) : ").find("Nemo"))
#Find returns -1 if it can't find the character or string in the given string

#Task 5 - examine the string to see if it starts or ends with a specific character
print(input("Give me a string so i can tell you if it starts with T : ").startswith("T"))
print(input("Give me a string so i can tell you if it ends with d : ").endswith("d"))

#Task 6 - you can check if the decimal, alphabetic , etc.
print(input("Give me a string so i can tell you if it is Decimal : ").isdecimal())
print(input("Give me a string so i can tell you if it is Numeric : ").isnumeric())
print(input("Give me a string so i can tell you if it is Alphabetical : ").isalpha())
print(input("Give me a string so i can tell you if it is Uppercase : ").isupper())
print(input("Give me a string so i can tell you if it is Lowercase : ").islower())

#Task 7 - Variables
#For example, we will create an identity:
firstName = "Unix"
lastName = "Torvalds"
alias = "Tux, coming from T(orvalds) U(ni)X"
age = "30"
cityOfLiving = "Helsinki, Finland"
parents = "Larry Ewing and Linus Torvalds"
dateOfBirth = "the 9th of May, in 1996"
race = "Penguin"
personalIdentificationNumber = "41819910"

#Task 8 - Printing The identity:
print("Hello, my name is " + lastName + " " + firstName + " ! \nPeople usually call me " + alias + " ! \nI am " + age + " and I come from  " + cityOfLiving + " ! \nMy parents are " + parents + " and I was born on" + dateOfBirth + " ! \nI am a " + race + " and my Personal Identification Number is " + personalIdentificationNumber + "!")

