'''
sort characters and numbers so that characters appears first then numbers
ex: input - AD431CZZ
output - ACDZZ134
'''

str=input("Enter string in format [A3D4S1]")

#creating two lists one for alphabets and other one for storing numbers
alpha=[]
num=[]

#iterating over each element in string to check whether it is alphabet or number
for ch in str:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num.append(ch)
#now ,we have separate list of alphabets and numbers
#sorting
sorted_list=sorted(alpha)+sorted(num)
print(sorted_list) #it is inn form of list

#list to string
output=''.join(sorted_list)

print(output)


