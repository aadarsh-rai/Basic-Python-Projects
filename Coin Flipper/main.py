#Coin FLippepr(Head or tail

import random

random_number  =random.randint(0,1) 

# heads=0 and tails = 1
result ="It's head"if random_number == 0 else "It's tail" #Using Ternary Operator
print(result)