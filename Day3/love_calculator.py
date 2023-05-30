print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
 
lower_name1 = name1.lower()
lower_name2 = name2.lower()
 
name = str(lower_name1) + str(lower_name2)
 
x=0
y=0
 
x += name.count("t")
x += name.count("r")
x += name.count("u")
x += name.count("e")
 
y += name.count("l")
y += name.count("o")
y += name.count("v")
y += name.count("e")
 
s = str(x) + str(y)
score = int(s)
#can also do - score = int(str(x) + str(y))
 
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")