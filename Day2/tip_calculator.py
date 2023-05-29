print("Welcome to the tip calculator!")
bill = float(input("What is your total bill?\n$"))
tip = int(input("What % would you like to give as a tip?\n"))
no = int(input("How many prople are splitting the bill?\n"))
 
total_bill = bill + (bill * (tip / 100))
per_person_bill = round((total_bill / no),2)
print(f"Each person should pay ${per_person_bill}")