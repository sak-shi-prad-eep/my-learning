num=int(input("Enter a number: "))
num=str(num).rstrip('0')
num1=num[::-1]
if num1==str(num):
    print("true")
else:
    print("false")

    