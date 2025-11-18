"""invert"""
# Invert Multi-Value Dictionary
# Problem:
# Given:
# courses = {
#     "Python": ["Alice", "Bob"],
#     "Java": ["Bob", "Charlie"],
#     "C++": ["Alice"]
# }
# Reverse the mapping so that each student lists all the courses they are enrolled in.
# Expected Output:
# {
#     "Alice": ["Python", "C++"],
#     "Bob": ["Python", "Java"],
#     "Charlie": ["Java"]
# }

courses = {
    "Python": ["Alice", "Bob"],
    "Java": ["Bob", "Charlie"],
    "C++": ["Alice"]
}



courses0={}
for x,y in courses.items():
    for j in y:
        # print(j)
        courses0.setdefault(j,[]).append(x)
print(courses0)


# courses1=[]
# for i in courses.items():
#     courses1.append(i)
# print(courses1)

# for i in range(len(courses1)):
#     # print(i)
#     for j in range(i+1,len(courses1)):
#         print(j)
