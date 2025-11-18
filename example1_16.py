"""merge"""
# Merge Deep Dictionaries
# Problem:
# You have two nested dictionaries:
# a = {"user": {"name": "John", "age": 25}, "status": "active"}
# b = {"user": {"age": 30, "email": "john@example.com"}, "role": "admin"}
#Merge them recursively so that values from b overwrite or extend a.
# Expected Output:
# {
#   "user": {"name": "John", "age": 30, "email": "john@example.com"},
#   "status": "active",
#   "role": "admin"}

# from collections import defaultdict

a = {"user": {"name": "John", "age": 25}, "status": "active"}
b = {"user": {"age": 30, "email": "john@example.com"}, "role": "admin"}

for x,y in b.items():
    if x in a and isinstance(b[x],dict):
        for x1,y1 in b[x].items():
            if x1 in a[x]:
                a[x][x1]=b[x][x1]
                # a[x].update({x1:b[x][x1]})
            else:
                # a[x].update({x1:b[x][x1]})
                a[x][x1]=b[x][x1]
    else:
        a[x]=b[x]
print(a)
