"""transform"""
# Transform Flat Keys to Nested Dict
# Problem:
# Convert this:
# flat = {
#     "user.name": "John",
#     "user.email": "john@example.com",
#     "address.city": "Austin",
#     "address.zip": "73301"}
# Into:
# {
#   "user": {"name": "John", "email": "john@example.com"},
#   "address": {"city": "Austin", "zip": "73301"}
# }

# from collections import defaultdict

flat = {
    "user.name": "John",
    "user.email": "john@example.com",
    "address.city": "Austin",
    "address.zip": "73301"}

flat1={}

for x,y in flat.items():
    # print(x,y)
    x1=x.split(".")
    x2=flat1
    for i in x1[:-1]:
        # print(i)
        if i not in x2:
            x2[i]={}
        x3=x2[i]
    x3[x1[-1]]=y

print(flat1)







# flat1={}

# for x,y in flat.items():
#     # print(x)
#     x1=x.split(".")
#     x2=flat1
#     for i in x1[:-1]:
#         # print(i)
#         if i not in x2:
#             x2[i]={}
#         x2=x2[i]
#     x2[x1[-1]]=y
# print(flat1)
