"""sort"""
# Sort Dictionary by Nested Value
# Problem:
# Sort the following dict by the nested 'score' field in descending order:
# students = {
#     "Alice": {"age": 25, "score": 88},
#     "Bob": {"age": 22, "score": 95},
#     "Charlie": {"age": 23, "score": 90}
# }
# Expected Output:
# {
#     "Bob": {"age": 22, "score": 95},
#     "Charlie": {"age": 23, "score": 90},
#     "Alice": {"age": 25, "score": 88}
# }

# from collections import defaultdict

students = {
    "Alice": {"age": 25, "score": 88}, #0
    "Bob": {"age": 22, "score": 95},   #1
    "Charlie": {"age": 23, "score": 90}#2
}

students1=[]
for x in students.items():
    students1.append(x)
print(students1)


for i,jaga in enumerate((students1)):
    for j in range(i+1,len(students1)):
        # print(j)
        if students1[i][1]["score"] < students1[j][1]["score"]:
            students1[i],students1[j]=students1[j],students1[i]
print(students1)

students2=dict(students1)
print(students2)
