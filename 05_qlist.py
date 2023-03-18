n=input()
m=len(n)
if m<3:
    print(n)
elif n[-3:]=="ing":
    print(n.replace("ing","ly"))
else:
    print(n+"ing")
