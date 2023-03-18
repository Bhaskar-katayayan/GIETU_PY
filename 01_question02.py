#  nearest palindrom number
def palin(n):
    temp=n
    while(1):
        if temp==(n==int(str(n)[::-1])):
             if n==int(str(n)[::-1]):
                 return n
        n+=1
n=int(input())
print(palin(n))

