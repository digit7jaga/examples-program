"""sorting challenge"""
# Sorting Challenge
# Question:
# Write a function to sort a list of words based on their length,
# and if lengths are equal, sort them alphabetically.
# Example:
# Input: ["apple", "bat", "ball", "ant"] → Output: ["ant", "bat", "ball", "apple"]

#input int and str, if int means skip >>>done


input1=["apple", "bat", "ball", "ant", "123"]
input2=[]

for i in input1:
    if i.isalpha():
        input2.append(i)

for i,a in enumerate(input2):#range(len(input2))
    for j in range(i+1,len(input2)):
        if input2[i]>input2[j]:
            input2[i],input2[j]=input2[j],input2[i]
        if len(input2[i])>len(input2[j]):
            input2[i],input2[j]=input2[j],input2[i]
print(input2)








# input=[]
# for i in input1:
#     if i.isalpha():
#         input.append(i)
# for i in range(len(input)):
#     for j in range(i+1,len(input)):
#         if input[i]>input[j]:
#             input[i],input[j]=input[j],input[i]
# print(input)
# for i in range(len(input)):
#     for j in range(i+1,len(input)):
#         if len(input[i])>len(input[j]):
#             input[i],input[j]=input[j],input[i]
# print(input)



# input0=[]
# for i in input:
#     if not i.isdigit():
#         input0.append(i)
# print(input0)
# input1={}
# for i in input0:
#     count=0
#     for j in i:
#         count+=len(j)
#     input1[i]=count
# print(input1)
# input2=list(input1.items())
# print(input2)
# for i in range(len(input2)):
#     print(i)
#     for j in range(i+1,len(input2)):
#         if input2[i]>input2[j]:
#             input2[i],input2[j]=input2[j],input2[i]
# print(input2)
# for i in range(len(input2)):
#     print(i)
#     for j in range(i+1,len(input2)):
#         # print(j)
#         if input2[i][1]>input2[j][1]:
#             input2[i],input2[j]=input2[j],input2[i]
# print(input2)
# result=[]
# for i in input2:
#     result.append(i[0])
# print(result)



# inputs=["apple", "bat", "ball", "ant","all"]#str(input("enter: "))
# array=[]
# for i in inputs:#.split(",")
#     array.append(i)
#     array.sort()
# s=sorted(array,key=lambda x:len(x))
# print(array)
# print(s)

# input=input("enter the inputs: ")
# array=[]
# for i in input.split(","):
#     s=i.strip()
#     array.append(s)
# # print(array)
# sorted_array=sorted(array,key=lambda x:len(x))
# print(sorted_array)
