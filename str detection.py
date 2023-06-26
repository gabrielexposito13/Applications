# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t_count_1 = name1.count("t")
r_count_1 = name1.count("r")
u_count_1 = name1.count("u")
e_count_1 = name1.count("e")

t_count_2 = name2.count("t")
r_count_2 = name2.count("r")
u_count_2 = name2.count("u")
e_count_2 = name2.count("e")

true_1_total = t_count_1 + r_count_1 + u_count_1 + e_count_1
true_2_total = t_count_2 + r_count_2 + u_count_2 + e_count_2
true_total = true_1_total + true_2_total

l_count_1 = name1.count("l")
o_count_1 = name1.count("o")
v_count_1 = name1.count("v")
e_count_1 = name1.count("e")

l_count_2 = name2.count("l")
o_count_2 = name2.count("o")
v_count_2 = name2.count("v")
e_count_2 = name2.count("e")

love_1_total = l_count_1 + o_count_1 + v_count_1 + e_count_1
love_2_total = l_count_2 + o_count_2 + v_count_2 + e_count_2
love_total = love_1_total + love_2_total

total = str(true_total) + str(love_total)
total = int(total)

condition1 = True if total <10 or total > 90 else False
condition2 = True if total >= 40 and total <= 50 else False

if condition1 == True:
    print(f"Your score is {total}, you go together like coke and mentos.")
if condition2 == True:
        print(f"Your score is {total}, you are alright together.")
if condition1 == False and condition2 == False:
      print(f"Your score is {total}")