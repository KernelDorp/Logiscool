#Task 1 - printing


myList = [ ]
for i in range(5):
    myList.append(input())
    for j in myList:
        print(j)
        #print in the same line
for k in myList:
    print(k , end = ' ')

#Task 2 - printing with sep
print("\nHello, Fellow code runners and IDEs. Please input something then smash enter, then type something else, smash enter again, type something else and then smash enter one last time so i can continue running, pretty please!")
a = input()
b = input()
c = input()
print(a, b, c, sep = '*')
#Task 3 - Converter
types = input("Converter type: (kg, c or km")
if types == "kg":
    x = float(input("The Value: "))
    unit = input("The unit: (kg / g)")
    if unit == "kg":
        print(str(x) + "kg in g: " + str(x * 1000))
    elif unit == "g":
        print(str(x) + "g in kg: " + str(x / 1000))
    else:
        print("Not a real unit.")
#Degrees
elif types == "c":
    x = float(input("The Value: "))
    unit = input("The unit: (c / f)")
    if unit == "c":
        print(str(x) + "Fahrenheit in Celsius: " + str(x * 1.8)+ 32)
    elif unit == "f":
        print(str(x) + "Celsius in Fahrenheit: " + str(x - 32) / 1.8)
    else:
        print("Not a real unit.")
#Miles & Kilometres
elif types == "km":
    x = float(input("The Value: "))
    unit = input("The unit: (km/m)")
    if unit == "km":
        print(str(x) + "km in m: " + str(x * 0.62137))
    elif unit == "m":
        print(str(x) + "m in km: " + str(x / 0.62137))
    else:
        print("Not a real unit.")

#Task 4 - Collatz
number = int(input())
collatz = [ ]
while number != 1:
    if number % 2 == 0:
        number /= 2
        collatz.append(int(number))
    else:
        number = number * 3 + 1
        collatz.append(int(number))
print(collatz)
#Password Checker
password = input("Enter A password: ")
characters = ["$", "&", "@", "#", "!"]
if (len(password) >= 6) and (len(password) <= 16):
    print("the length is good ")
    if i.islower():
        print("there is a lower case ")