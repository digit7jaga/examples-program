"""sorting"""
# Sort strings by number of vowels (descending)
# words = ["banana", "apple", "grape", "kiwi", "strawberry"]

#IF AEIOU NOT  in input means it donot come in output >>> done

from collections import deque
import re

words = ["strawberry","shailesh","aeiou","AEIOU","12345","try"]
vowels=["a","e","i","o","u"]
array=[]

for i in words:
    if i.isalpha() :
        if any(x in i.lower() for x in vowels):
            array.append(i.lower().strip().replace(" ",""))
print(array)

b={}
c=deque()

for i in array:
    COUNT=0
    for j in i:
        if re.search("[aeiou]",j):
            COUNT+=1
    b[i]=COUNT
print(b)


d=[]
for i in b.items():
    d.append(i)
print(d)

for i,jaga in enumerate((d)):
    for j in range(i+1,len(d)):
        if d[i][1]>d[j][1]:
            d[i],d[j]=d[j],d[i]
print(d)

e=[]
for i in d:
    e.append(i[0])
print(e)








# while b:
#     max_word = max(b, key=b.get)
#     c.appendleft(max_word)
#     del b[max_word]

#     # maxed=max(x)
#     # c.append(maxed)

# # max=0
# # for x,y in b.items():
# #     if y>=max:
# #         c.append(x)
# #     else:
# #         pass
# print(c)














# def count_vowels(n):
#     return sum(1 for i in n if i in a)
# sorted_array = sorted(array, key=count_vowels,reverse=True)
# print(sorted_array)


# sorting=False
# for j in array:
#     count=0
#     for i in j:
#         if i in a:
#             count+=1
#             sorting=True
#             print("yes")
