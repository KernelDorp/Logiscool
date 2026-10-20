def ifNotInName():
    print("Ahhhhhh, Your name is not in my list! I Couldn't Guess it! You won my game!")
    name.lower()
    name.capitalize()
    names.append(name)
#Task 1
for i in range(10):
    print(i)


print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#Task 2
for i in range(2, 100, 2):
    print(i)

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#Task 3
for i in "Buna Seara.":
    print(i)

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#Task 4
num = int(input("Give me a number"))
for i in range (1, 11, 1):
    print(str(i) + " * " + str(num) + " = " + str(i * num))

#Task 5
enc = "Wyh earne  eclaenp hIa nbtu?"
dec = " "
for i in range(0, len(enc)):
    if i % 2 == 0:
        dec += enc[i]
for i in range(0,len(enc)):
    if i % 2  == 1:
        dec += enc[i]
print(dec)
print(enc)


#Task 6

enc2 = "Ic hU,s eB TAWr!"
dec2 = " "
for i in range(0, len(enc2)):
    if i % 2 == 0:
        dec2 += enc2[i]
for i in range(0,len(enc2)):
    if i % 2  == 1:
        dec2 += enc2[i]
print(dec2)
print(enc2)

#Task 7
list1 = [ ]
for i in range(50):
    list1.append(i)
print(list1)
#Task8
list2 = [ ]
for k in range(7, -20, -1):
    list2.append(k)
print(list2)

#Task9
names = ['Ana', 'Marius' , 'Alex' , 'Andrei']
name = input("Give me a Name")
for item in names:
    if item.lower() == name.lower():
        print("The Name is already in my list! I Have Guessed Your name! Yay!")
    else:
        ifNotInName()
        break

#Task 10
for i in range(11):
    for j in range(11):
        print(str(i) + " * " + str(j) + " = " + str(i * j))
        j += 1
    i += 1