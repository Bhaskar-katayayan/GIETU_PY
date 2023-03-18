n=input()
count1=0
count2=0
m2=[]
for i in n:
	if (i.isalpha()):
		count1 +=1
	elif i.isdigit():
		count2 +=1
	else:
		continue
m2.append(count1)
m2.append(count2)
print(m2)

#02 second method
# def function(n):
# count1=0
# count2=0
# for i in n:
# 	if (i.isalpha()):
# 		count1 +=1
# 	elif i.isdigit():
# 		count2 +=1
# 	else:
# 		continue