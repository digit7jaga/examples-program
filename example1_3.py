"""find missing no in sequence"""
# Find Missing Number
# Question:
# Given a list of integers from 1 to n with one missing number, find the missing number.
# Example:
# Input: [1, 2, 4, 5, 6] → Output: 3

inputs=[1, 2, 4, 5, 6]

# for i in range(len(inputs)-1):
#     print(i)
diff=[inputs[i+1]-inputs[i] for i in range(len(inputs)-1)]
print(diff)

commondiff=max(set(diff),key=diff.count)
# print(commondiff)

for i,j in enumerate(diff):#range(len(diffs)),
    if diff[i] != commondiff:
            # Return the expected number at the break
        print(inputs[i]+1)










# def Finds(inputs):
#     a=str(inputs).split(",")
#     b=len(a)+1
#     formula=int(b*(b+1)/2)
#     return formula - sum(int(i) for i in a)
# inputs=input("enter: ")
# print(Finds(inputs))

# def find(inputs):
    # s = str(inputs)
    # n = len(s) + 1
    # total = n * (n + 1) // 2
    # return total - sum(int(digit) for digit in s)
# inputs = int(input("Enter the inputs: "))
# missing = find(inputs)
# print("Missing no is:", missing)
