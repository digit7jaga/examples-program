"""sort"""
# Sort List of Dictionaries by Multiple Keys (Nested)
# Problem:
# Sort a list of employees by department, then by salary descending, and finally by name ascending.
# employees = [
#     {"name": "Alice", "dept": "Sales", "salary": 70000},
#     {"name": "Bob", "dept": "HR", "salary": 40000},
#     {"name": "Charlie", "dept": "Sales", "salary": 80000},
#     {"name": "David", "dept": "HR", "salary": 50000},
# ]

employees = [
    {"name": "Alice", "dept": "Sales", "salary": 70000},#0
    {"name": "Bob", "dept": "HR", "salary": 40000},     #1
    {"name": "Charlie", "dept": "Sales", "salary": 80000},#2
    {"name": "David", "dept": "HR", "salary": 30000},      #3
]


# x=sorted(employees,key=lambda x:(x["dept"]))
# employees=x
# print(employees)

# y=sorted(employees,key=lambda x:(x["salary"]))
# employees=y
# print(employees)

for i,jaga in enumerate((employees)):
    # print(i)
    for j in range(i+1,len(employees)):
        # print(j)
        if employees[i]["dept"]>employees[j]["dept"]:
            if (employees[i]["dept"]==employees[j]["dept"] and
                (employees[i]["salary"]>employees[j]["salary"])):
                employees[i],employees[j]=employees[j],employees[i]
print(employees)


# for i in range(len(employees)):
#     for j in range(i+1,len(employees)):
#         if employees[i]["salary"]>employees[j]["salary"]:
#             employees[i],employees[j]=employees[j],employees[i]
# print(employees)
