n=input()
n2=(int(n)*2)
n3="".join(sorted(str(n)))
n4="".join(sorted(str(n2)))
print(n3)
print(n4)
if len(str(n))==len(str(n2)) and n3==n4:
    print(True)
else:
    print(False)
