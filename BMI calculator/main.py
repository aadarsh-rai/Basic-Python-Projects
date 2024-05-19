#BMi Calculator 2.0

height = float(input("Enter your height in meter(m): "))
weight = float(input("Enter your weight in Kilogram(kg): "))

bmi = weight/(height ** 2)
print()

if bmi < 18.5:
    print(f"Your bmi({round(bmi, 2)}) is in  underweight category")
elif bmi > 18.5 and bmi <25:
    print(f"Your bmi({round(bmi, 2)}) is in normal weight category")
elif bmi >= 25 and bmi <= 30:
    print(f"Your bmi({round(bmi, 2)}) is in overweight category")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi({round(bmi, 2)}) is in obese category")
elif bmi > 35:
    print(f"Your bmi({round(bmi, 2)}) is in clinically obese category")