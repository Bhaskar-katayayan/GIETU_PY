n=input()
m1=len(n)
if m1<2:
    print(-1)
elif m1==2:
    print(n*2)
else:
    # print(n[:2], end="")
    # print(n[-2:])
    l=n[:2]+n[-2:]
    print(l)