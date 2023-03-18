list1=[" a new world record was set", " in the holy city of ayodhya", "on the eve of diwali on tuesday",
       "with over three lakh diya or earthen lamps","lit up simulaneously on the banks of the sarayu river"]
stopwords=[ "for","a","of","the","and","to","was","in","on","with"]
result=[]
for i in list1:
    rw=[]
    for j in i.split():
        if j not in stopwords:
            rw.append(j)
    result.append(rw)
print(result)

print([[j for j in i.split() if j not in stopwords] for i in list1])