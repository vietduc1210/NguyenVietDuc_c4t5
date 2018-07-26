weight = int(input("weight(kg) = "))
height = int(input("height(cm) ="))
height_m = height/100

BMI = weight/(height_m**2)
print("BMI =" , BMI)
if BMI < 16 :
    print("Severely underweight")
elif 16 <= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")