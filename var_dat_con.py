# ATM Withdrawal
balance = 50000
amount = int(input("enter amount:"))
if amount <= balance:
    print("withdrawal sucessful")
else:
    print("Insufficient balance")

# movie ticket eligibility
age = int(input("enter age:"))
if age>=18:
    print("eligible to ticket booking")
else:
    print("not eligible to ticket booking")

# BMI weight checker
weight = float(input("enter weight:"))
height = float(input("enter height:"))
BMI = weight / (height*height)
print("BMI:",BMI)
if BMI <= 18.5:
    print("under weight")
elif BMI <=25:
    print("normal weight")
else:
    print("obisity")
          