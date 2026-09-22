my_name = "Matei"
my_age = 12
t_age = "42"
p_age = "30"
t_name = "Testosul"
p_name = "TUX"


print("My name is "+ my_name + ".\nI am " + str(my_age) +  ".\n")
print("My first pet is " + p_name + ", he's a " + p_age + "y/o penguin, and the mascot of Linux.")
print("My second pet is "+ t_name + "he's a " + t_age + "y/o turtle, and my friend's favourite animal")
print("My name is %a and I am a %sy/o" %(my_name, my_age))
action1 = input("Give me an action.")
enemy1 = input("Give me a bad character.")
character1 = input("Give me your favourite character.")
item1 = input("Give me an item.")
supermarket1 = input("Give me a supermarket name.")
quote1 = input("Give me a funny text")
print("Here is a funny story that has been generated from your responses:\n \n")

print("""
I was %s, and then %s came and attacked me.
Then, %s spawned and saved me,
Afterwards, I bought him a %s from %s for saving me,
He thanked me and said %s""" %(action1, enemy1, character1, item1, supermarket1, quote1))

a = input("Give me a number for the Variable A")
b = input("Give me a number for the Variable b")
if a>b:
    print("%s is Bigger than %s" %(a,b))
elif a<b:
    print("Number %s is smaller than %s" %(a, b))
else:
    print("Numarul %s este egal cu %s" %(a,b))

nota = input("Scrie o nota intre 10-100")
if int(nota) > 50:
    if int(nota) > 75:
        print("Ai luat nota FB")
    else:
        print("Ai luat nota B")
else:
    if int(nota) > 25:
        print("Ai luat nota S")
    else:
        print("Ai luat nota I")

