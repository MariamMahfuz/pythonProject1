num1=int(input("Enter Your First Num:"))
num2=int(input("Enter Your Second Num:"))
num3=int(input("Enter Your Third Num:"))
if num1>num2 and num2>num3:
    print("First Num is the largest num")
elif num2>num1 and num1>num3:
    print("Second Num is the largest num")
else:
    print("Third Num is the largest num")
