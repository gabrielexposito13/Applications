import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

#Slices the input into separate strings by the comma and a space: 
names = names_string.split(", ")

#This counts the amount of names inputed above: 
num_items = len(names)

#Random selector within inputed names: 
random_choice = random.randint(0, num_items - 1)

#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")