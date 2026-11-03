#Task 1 - hangman
puzzle = "computer science"
penguins = "🐧🐧🐧🐧🐧🐧"
my_solution = "________ _______"
correct_letters = []
incorrect_letters = []
life = 10
print(penguins)
while life > 0 and puzzle != my_solution:
    print(my_solution)
    guess = input("Type a new letter: \n")
    if len(guess) == len(puzzle):
        temp = my_solution
        my_solution = guess
        print("HAHHAHA, you tried to guess my puzzle, and....")
        print("Your guess is...... ")
        if my_solution == puzzle:
            print("Correct!")
        else:
            print("Wrong! HAHHAHAH! You loose one life")
            life -= 1
            print("This isn't in the puzzle. %s lives left. " %(str(life)) )
    else:
        found_something = False
        for i in range(len(puzzle)):
            if puzzle[i] == guess:
                my_solution_list = list(my_solution)
                my_solution_list[i] = guess
                my_solution = "".join(my_solution_list)
        if not found_something:
            incorrect_letters.append(guess)
            life -= 1
            print("This isn't in the puzzle. %s lives left. " %(str(life)))
        else:
            correct_letters.append(guess)
        print("List of correct letters : %s. \nList of incorrect letters: %s" %(str(correct_letters), str(incorrect_letters)))
if life > 0:
        print("Congratulations")
else:
        print("Maybe next time")

#Task 2 - greatest common divisor (c.m.m.d.c.)

n1 = int(input("What is the 1st number?\n"))
n2 = int(input("What is the 2nd number?\n"))
gcd = 1
for i in range(1, n1 + 1):
    if n1 % i == 0 and n2 & i == 0:
        gcd = 1
print("Da greatest common divisor of %s and %s is %s. " %(str(n1), str(n2), str(gcd)))