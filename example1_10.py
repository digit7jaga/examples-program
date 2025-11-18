"""sort"""
# Sort nested lists by the sum of inner elements
#  lists = [[5, 2], [1, 9, 3], [4], [10, 0, -1]]

lists= [[5, 2], [1, 9, 3], [4], [10, 0, -1]]
# print(lists)
# # sorted=sorted(lists,key=sum)
# # print(sorted)


print(lists)
for i,jaga in enumerate((lists)):
    for j in range(i+1,len(lists)):
        if sum(lists[i])>sum(lists[j]):
            lists[i],lists[j]=lists[j],lists[i]
print(lists)
