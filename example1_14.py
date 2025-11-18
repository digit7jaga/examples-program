"""sort"""
# Sort a String by Character Frequency (Descending)
# Problem:
# Sort characters of a string by frequency descending, and if equal, by alphabetical order.
# s = "treehouse"
# Output: "eeeohsrut"

S = "treehouse"

s1={}
for i in S:
    if i in s1:
        s1[i]+=1
    else:
        s1[i]=1
print(s1)

s2=[]
for i in s1.items():
    s2.append(i)
print(s2)

for i,jaga in enumerate((s2)):
    for j in range(i+1,len(s2)):
        if s2[i][1]<s2[j][1]:
            s2[i],s2[j]=s2[j],s2[i]
print(s2)

s3=[]
for i in s2:
    s3.append(i[0]*i[1])
print(s3)
