"""sort"""
# Sort based on frequency (most frequent first)       data = [5, 1, 2, 1, 3, 2, 2, 5, 5, 5]

# from collections import Counter
# from statistics import mode

data = [5,1,2,1,3,2,2,5,5,5,4]
# c=Counter(data)
# print(c)

# d=mode(data)
# print(d)

data2=[]
for i in data:
    data2.append(str(i))

for i,jaga in enumerate((data2)):
    # print(type(i),i)
    # ins=int(i)
    # count=0
    for j in range(i+1,len(data2)):
        # print(j)
        if data2[i]>data2[j]:
            data2[i],data2[j]=data2[j],data2[i]
print(data2)

data3={}
for i in data:
    if i in data3:
        data3[i]+=1
    else:
        data3[i]=1
print(data3)

data4=[]
for i in data3.items():
    data4.append(i)
print(data4)

for i,jaga in enumerate((data4)):
    for j in range(i+1,len(data4)):
        if data4[i][1]<data4[j][1]:
            data4[i],data4[j]=data4[j],data4[i]
print(data4)

data5=[]
for i in data4:
    data5.append(i[0])
print(data5)






# for i in data:
    # if i == i:
    #     data1.append(i)
# while data:
#     maxx= max(data,key=data.sort())
#     data1.append(maxx)

# print(data1)
