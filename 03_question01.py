mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
rw=[]
for i in list_b:
        rw.append((i, mylist.index(i)))
print(rw)

print({ i:mylist.index(i) for i in list_b})

rw={}
for i in list_b:
        rw[i]= mylist.index(i)
print(rw)
