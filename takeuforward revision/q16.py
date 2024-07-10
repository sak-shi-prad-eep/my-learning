num=int(input("Enter a number: "))
num=str(num).rstrip('0')
list1=''.join(num)
print(list1[::-1])