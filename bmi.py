height=float(input("Enter ur height(in meters):"))
weight=float(input("Enter ur weight(in kgs):"))
bmi=weight/height**2
print(bmi)
if bmi<16:
    print("underweight")
elif bmi>18 and bmi<25:
    print("Noraml Weight ")
elif bmi>25 and bmi<30:
    print("Pre-Obesity")
elif bmi>30 and bmi<35:
    print("Obesity class I")   
elif bmi>35 and bmi<40:
    print("Obesity class II")
elif bmi>40:
    print("Obesity class III")