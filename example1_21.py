"""group"""
# Group by Multiple Keys
# Problem:
# Group this list of dicts by both department and role:
# records = [
#     {"name": "Alice", "department": "IT", "role": "Developer"},
#     {"name": "Bob", "department": "HR", "role": "Recruiter"},
#     {"name": "Eve", "department": "IT", "role": "Developer"},
#     {"name": "John", "department": "IT", "role": "Manager"}
# ]
# Expected Output:
# {
#   ("IT", "Developer"): ["Alice", "Eve"],
#   ("HR", "Recruiter"): ["Bob"],
#   ("IT", "Manager"): ["John"]
# }

from collections import defaultdict

records = [
    {"name": "Alice", "department": "IT", "role": "Developer"},
    {"name": "Bob", "department": "HR", "role": "Recruiter"},
    {"name": "Eve", "department": "IT", "role": "Developer"},
    {"name": "John", "department": "IT", "role": "Manager"}
]

output=defaultdict(list)

for i in records:
    # print(i)
    i1=i["department"],i["role"]
    output[i1].append(i["name"])

# for i in output.items():
#     print(i)
# print(output,type(output))

output1=dict(output)
print(output1)

#hiiiiiiiiiiiiiiiiiiiiiiiiii