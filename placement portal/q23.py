import re
email=input()
pattern=r'^([\w\.-]+)@([\w\.-]+)\([a-zA-Z]{2,})$'
match=re.match(pattern,email)
print(match.group(1),match.group(2),match.group(3))