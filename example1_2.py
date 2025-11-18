"""sum of digits"""
# Sum of Digits
# Question:
# Given a number, return the sum of its digits until the result is a single digit.
# Example:
# Input: 9875 → Output: 2 (9+8+7+5=29 → 2+9=11 → 1+1=2)

#check how many characters in input >>>
# File "c:\Users\Jagadeesh_D7\Desktop\examples1\example1_2.py", line 19, in <module>
#     inputs=int(input("enter: "))
# ValueError: Exceeds the limit (4300 digits)
#  for integer string conversion: value has 33138 digits;
# use sys.set_int_max_str_digits() to increase the limit

def digits(n):
    """sum of digits"""
    ins=str(n).strip()
    try:
        if len(ins)<=1:
            return ins
        else:
            sums=0
            for i in ins:
                sums+=int(i)
        return digits(sums)
    except (ValueError,TypeError) as e:
        return ("error!!",e)

inputs=int(input("enter: "))
inputs1=digits(inputs)
print(inputs1)









# inputs=int(input("enter the inputs: "))
# ins=str(inputs)
# sum=0
# for i in ins:
#     sum+=int(i)
#     s=str(i)
# print(sum)

# def sums(inputs):
#     ins=str(inputs)
#     if len(ins)<=1:
#          return ins
#     else:
#      sum=0
#      for i in ins:
#         sum+=int(i)
#     return sums(sum)
# inputs=int(input("enter the inputs: "))
# print(sums(inputs))
