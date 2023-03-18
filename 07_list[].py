try:
    n=[]
    while True:
        n.append(int(input()))
except:
    print(tuple(n))
x=list(n)
sum1=sum(n)
avr=(sum1//len(n))
print(avr)
lew=len(n)
count=0
for i in n:
    if i>avr:
        count+=1

sum2=((count/lew)*100)
print(sum2)
lom=sorted(n)
freq=[]
for x in range(lew):
    count=0
    for y in n:
        if x==y:
            count+=1
    freq.append(count)
    # print(sum2)
    print(freq)
print(list(lom))