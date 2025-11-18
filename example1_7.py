"""sort"""
# Sort list of numbers by their digit sum   numbers = [12, 45, 7, 111, 39, 24]

#if str i input means donot allow >>> done
numbers=[12, 45, 7, "111", 39, 24]
numbers0=[]
numbers2={}

for i in numbers:
    if isinstance(i,int):
        numbers0.append(i)
print(numbers0)


for i in numbers0:
    # print(type(i),i)
    S=str(i)
    numbers1=[]
    for j in S:
        numbers1.append(int(j))
        digitsum=sum(numbers1)
    numbers2[i]=digitsum
print(numbers2)

numbers3=list(numbers2.items())

for i,jaga in enumerate(numbers3):#for i in range(len(numbers3))
    print(i)
    for j in range(i+1,len(numbers3)):
        if numbers3[i][1]>numbers3[j][1]:
            numbers3[i],numbers3[j]=numbers3[j],numbers3[i]
print(numbers3)

numbers4=[]
for i in numbers3:
    numbers4.append(i[0])
print(numbers4)








# inputno=[12,45,7,111,39,24]
# def counts(n):
#     return sum(int(j) for j in str(n))
# sorted=sorted(inputno,key=counts)
# print(sorted)

# inputs=str(input("enter:" ))
# for i in inputs.strip().split(","):
#     inputno.append(int(i))
# print(inputno)
