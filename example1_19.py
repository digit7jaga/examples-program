"""detect"""
# Detect Duplicates in Dict List
# Problem:
# Given:
# employees = [
#     {"id": 101, "name": "Alice"},
#     {"id": 102, "name": "Bob"},
#     {"id": 101, "name": "Alice"},
#     {"id": 103, "name": "Eve"}
# ]
# Find all employees with duplicate IDs.
# Expected Output:
# [{"id": 101, "name": "Alice"}]

employees = [
    {"id": 101, "name": "Alice"},
    {"id": 102, "name": "Bob"},
    {"id": 101, "name": "Alice"},
    {"id": 103, "name": "Eve"}
]

employees1=[]

for i,jaga in enumerate((employees)):
    # print(i)
    for j in range(i+1,len(employees)):
        # print(j)
        if employees[i]["id"]==employees[j]["id"]:
            employees1.append(employees[i])
print(employees1)
