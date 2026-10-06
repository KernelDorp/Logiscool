#Task1 - while loop that repeats forever
from numpy.random import randint

number = 1
stop = int(input("At What number do you want the count to stop?"))
plusWhat = int(input("Plus what value should the number increase per loop?"))
while True and number <= stop:
    print(number)
    number += 1


#Task 2 - print only the first 10 integers and calculate the sum of these numbers
number = 1
sumIs = 0
while number < 11:
    print(number)
    sumIs += number
    number += 1
print(sumIs)


#Task 3 - Number of digits in a number
number = 836170926
originalNumber = number
count = 0
while number != 0:
    number //= 10
    print(number)
    count += 1
print("number of digits for the number %s : %s" %(originalNumber, count) )

#Task 4 - number guessing game
num = randint(0,100)
guessnum = int(input('How Many guesses should we have? '))
guess = 0

while guessnum > 0 and guess != num:
    guess = int(input("Take a guess: \n"))
    if guess > num:
        print("I though of a smaller number.")
    elif guess < num:
        print("I thought of a bigger number.")
    guessnum -=1
    print("You have won " + str(guessnum) +  " chances left")

print("Question: Why didn't we verify the case of equality in the if-else?")
print("Answer: Because it is one of the running condition of the while loop")

if guess == num :
    print("Congratulations, the number I thought of, was " , str("num"))
else:
    print("Maybe next time ,The nuber I thought if was " , str(num))

#Task 5 -  Fibonacci sequence
counter = 10
num1 = 0
num2 = 1
print("Fibonacci sequence: ")
while counter > 0:
    print(str(num1),"\n")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1
