#Tip Calculator

print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip = input("What percetage tip would you like to give? ")
people = input("How many people are splitting the bill? ")

tip_perc = int(tip) / 100
total_and_tip = (tip_perc*int(total)) + int(total)
per_person_pay = round(total_and_tip / int(people), 2)

print(f"Each person should pay: ${per_person_pay}")