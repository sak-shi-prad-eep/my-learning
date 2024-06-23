string1=input()
words=string1.split()
new=[i for i in words if i.lower()!="the"]
result=' '.join(new)
print("Result string is")
print(result)