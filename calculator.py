#SIMPLE CALCULATOR
operator=input("enter the operator (+,-,*,/):")
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
if operator=="+":
    print(f"{num1}+{num2}={num1+num2}","\nThankyou for using calculator")
elif operator =="-":
    print(f"{num1}-{num2}={num1-num2}","\nThankyou for using calculator")
elif operator=="*":
    print(f"{num1}*{num2}={num1*num2}","\nThankyou for using calculator")
elif operator=="/":
        print(f"{num1}/{num2}={num1/num2}","\nThankyou for using calculator")
else:
     print("invalid operator!!\n thankyou for using calculator")
