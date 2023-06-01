import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num = len(names)
rand = random.randint(0,num - 1 )
payer = names[rand]
print(f"{payer} is going to buy the meal today!")

#payer = random.choice(names)
#print(f"{payer} is going to buy the meal today!")