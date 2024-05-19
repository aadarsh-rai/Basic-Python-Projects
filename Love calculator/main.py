#Love Calculator

print("Welcome to the Love Calculator")

name1= input("What is your name?\n")
name2= input("What is their name?\n") 

lower_name1 =name1.lower()
lower_name2 =name2.lower()

combined_name = lower_name1 +lower_name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u +e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v +e 

love_score = str(true) + str(love)
print(love_score)

if int(love_score) < 10 or int(love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos")
elif int(love_score) >= 40 and int(love_score) <= 50:
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}")