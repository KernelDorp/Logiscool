#Lists can be used to store multiple pieces of info in one variable
#lists are a separate data type in Python
# the elements of the list are ordered
# lists can be modified and contain duplicated elements
# there is no limit for how many elements there are in a list
# indexing start from the first element, which gets the number 0, the next one is 1, 2 etc.
import time

#Task 1- Create a list with manually added items and print the elements
names = ["Matei", "Tux", "Tudor", "Testosul", "Penny", "Linus Torvalds", "Linux" , "Linus Tech Tips" ]
print(names)
print(type(names))
print("")

#Task 2 - length function
print("The list of your list is %s" %(str(len(names))))
print("")
#Task 3 - first, last and chosen element
print(names[0])
#the first element in a list, is the index number 0
#the number 0 represents the first number in a series.

print(names[-1]) #last element
print(names[3]) #chosen element
print("")

#Task 4 - list slicing
print(names)
print(names[0:4])
#when we're slicing, we're taking away the elements from the first element in the square parentheses, for example [0:4], from index element 0, to the one before the last number, in the previous example, we had four, so we cut the list at the index number 3 of the list.
print(names[:2])
#if the first number isn't specified, it means from the first element in the list (index number 0), to the number specified, in the example before, it was from the first element in the list, to the 1st element in the list.
print(names[2:])
#if the second number isn't specified, it means that we start from the first number, so in our example, we start from number 2, to the last element in the list.
print(names[2:-1])
print(names[2:-2])

#Task 5 - using a loop to print each element from the list
i = 0
while i < len(names):
    print(names[i])
    i += 1
print("\nOh, well, hello, fellow code runner, please, use Linux, for your own safety, privacy, and sanity, please, I beg you, use Linux. I, as a 12y/o use Arch myself, so please, use Linux! Thank you, now returning to my code:\n")
time.sleep(10)
#Task 6 - create a new list and fill it with the first 50 positive integers
numbers = [ ]
i = 1
while i <= 50:
    numbers.append(i)
    i += 1
    print(numbers)

#Task 7 -  create a new list, which contains the first 10 odd numbers and another list for the first 10 even numbers
on = [ ]
en = [ ]
i = 0
while i <= 20:
    if i % 2 == 1:
        on.append(i)
    else:
        en.append(i)
    i += 1
    print("Odd numbers are: %s\nAnd the even numbers are: %s" %(on, en))

#Task 8 - insert items into a list
insertList = [ ]
insertList.insert(0, "Logiscool")
insertList.insert(1 , "fun")
#Nice
insertList.insert(1 , "is" )
insertList.insert(5 , "everyone")
insertList.insert(3, "for")
print(insertList)

