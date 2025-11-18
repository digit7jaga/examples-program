"""dictionary"""
# Dictionary Comprehension
# Question:
# Given a list of student names and scores,
# create a dictionary with only students who scored above50.
# Example:
# Input: {'John': 45, 'Alice': 80, 'Bob': 60} → Output: {'Alice': 80, 'Bob': 60}

#check the type (isinstance()) >>> done

# import json

# scores = json.loads(input("enter: "))
scores = {'John': 45, 'Alice': 80, 'Bob': 60}
# filtered_scores = {} #name: score for name, score in scores.items() if score > 50


# try:
#     if isinstance(scores,dict):
#         for x,y in scores.items():
#             if y>50:
#                 filtered[x]=y
# except Exception as e:
#     print(e)

# print(scores)

# scores={x:y for x,y in scores.items() if y>50 and isinstance(scores,dict)}
# print(scores)

# score=lambda x:{k:v for k,v in x.items() if v>50}
# print(score(scores))

try:
    scores={x:y for x,y in scores.items() if y>50 and isinstance(scores,dict)}
    print(scores)
except (ValueError,TypeError) as e:
    print("error",e)
# finally:
#     print(scores)
