'''
list_li = []
n = int(input("Enter the value of n"))
for i in range(n):
   # x = int(input("Enter the value"))
    list_li.append(int(input("Enter the value in list")))
print(list_li)
'''

def commas(str):
    x = ','.join(str)
    return x

print(commas("Apple"))
z