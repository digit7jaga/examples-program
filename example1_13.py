"""sort"""
# Sort Nested List by Sum of Elements
# Problem:
# Given a list of lists, sort them based on the sum of elements, and if sums are equal, by length.
# lists = [[5, 2], [1, 2, 3], [3, 3], [10], [1, 1, 1, 1]]

lists = [[5, 2], [1, 2, 3], [3, 3], [10], [1, 1, 1, 1]]


for i,jaga in enumerate((lists)):
    for j in range(i+1,len(lists)):
        if sum(lists[i])>sum(lists[j]):
            lists[i],lists[j]=lists[j],lists[i]
print(lists)
