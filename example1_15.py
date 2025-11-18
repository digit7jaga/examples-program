"""counter"""
# Nested Frequency Counter
# Problem:
# You are given a list of dictionaries like:
# data = [
#     {"city": "New York", "fruit": "apple"},
#     {"city": "Paris", "fruit": "apple"},
#     {"city": "Paris", "fruit": "banana"},
#     {"city": "New York", "fruit": "apple"},
# ]
# Create a dictionary that shows how many times each fruit appeared per city.
# Expected Output:
# {
#   "New York": {"apple": 2},
#   "Paris": {"apple": 1, "banana": 1}
# }

from collections import defaultdict

data = [
    {"city": "New York", "fruit": "apple"},  #0
    {"city": "Paris", "fruit": "apple"},     #1
    {"city": "Paris", "fruit": "banana"},    #2
    {"city": "New York", "fruit": "apple"},  #3
]


frequency={}

for i in data:

    key=(i["city"],i["fruit"])
    if key in frequency:
        frequency[key]+=1
    else:
        frequency[key]=1
print(frequency)

output=defaultdict(dict)

for (x,y),z in frequency.items():
    output[x][y]=z

print(output)



# frequency1={}
# for i in frequency:
#     key1=i
#     if key1 in frequency1:
#         frequency1[key1]+=1
#     else:
#         frequency1[key1]=1
# print(frequency1)



# for i in range(len(data)):
#     count=0
#     print(i)
#     for j in range(i+1,len(data)):
#         if data[i]["city"]==data[j]["city"]:
#             if data[i]["fruit"]==data[j]["fruit"]:
#                 count+=1
#             else:
#                 count=1
#         else:
#             count=1
#     frequency[i]=count
#         # if i in frequency:
#         #     frequency["fruit"]+=1
#         # else:
#         #     frequency["fruit"]=1
# print(frequency)
