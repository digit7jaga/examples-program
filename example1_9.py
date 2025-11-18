"""sort"""
# Sort strings by the position of their first vowel
# words = ["try", "sky", "apple", "orange", "grape", "fly"]

import re
# from collections import deque

words = ["try", "sky", "apple","grape","orange", "cable", "fly"]
vowel={"a","e","i","o","u"}
end=[]
end1=[]
end2=[]

for i in words:
    word=i.lower().split(",")
    for j in word:
        j1=j.split(",")
        if re.search("[aeiou]",j[0]):
            end.append(j)
        if re.search("[aeiou]",j[1]):
            end.extend(j1)
        # if re.search("[aeiou]",j[2]):
        #     end.append(j1)
        if re.search("[aeiou]",j):
            if j not in end:
                end1.append(j)
        if j not in end:
            if j not in end1:
                end2.append(j)
#         else:
#             pass

end.extend(end1)
end.extend(end2)
print(end)


# for i in words:
#     word=i.lower().split(",")
#     for j in i.lower().split(","):
#         if re.search("[aeiou]",j[0]):
#             end.append(j)
#         if re.search("[aeiou]",j[1]):
#             end.extend(j.split(","))
#             if re.search("[aeiou]",j[2]):
#                 end.extend(j.split(","))

#         if re.search("[aeiou]",j):
#             if j not in end:
#                 end1.append(j)
#         if j not in end:
#             if j not in end1:
#                 end2.append(j)
#         else:
#             pass

# end.extend(end1)
# end.extend(end2)
# print(end)
# print(end1)
# print(end2)
