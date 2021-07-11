num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
num3 = int(input("Enter your third number:"))
if num1>num2 || num2>num3:
    print( " First Number is the largest number")
elif num2>num1||num1>num3:
    print( " Second Number is the largest number")
else:
    print(" Third Number is the largest number ")
