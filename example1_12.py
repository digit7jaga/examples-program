"""sort"""
# Sort Mixed Data Types (Numbers + Strings)
# Problem:
# You have a list containing both integers and strings representing numbers.
# Sort them numerically, treating all as numbers.
# data = [10, '5', '20', 3, '100']

data = [10, '5', '20', 3, '100']

data1=[]

for i in data:
    data1.append(int(i))

for i,jaga in enumerate((data1)):
    for j in range(i+1,len(data1)):
        if data1[i]>data1[j]:
            data1[i],data1[j]=data1[j],data1[i]
print(data1)
