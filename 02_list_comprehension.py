# List comprehension

# for loop version

# result=[]
# for i in range(11):
#     result.append(i)
# print(result)

# # list comprehension version

# print([i for i in range(11)])

# # for loop odd version

# result=[]
# for i in range(11):
#     if i%2 !=0:
#         result.append(i)
#     else:
#         result.append(i**2)
# print(result)
# print([i for i in range(11) if i%2!=0])

# print([i if i%2!=0 else i**2 for i in range(11)])

# question_01

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in mat:
    row_data=[]
    for j in i:
        
        if j%2!=0:
            row_data.append(j**2)
        else:
            row_data.append(j**3)
    result.append(row_data)
print(result)

print([elem**2 if elem%2!=0 else elem%3 for row in mat for elem in row])
print([[elem**2 if elem%2 !=0 else elem**3 for elem in row] for row in mat])