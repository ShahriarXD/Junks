import ast
dict1 = {'a': 10, 'b':20, 'c':30}
dict2 = {'a': 10, 'c':20, 'd':30, 'e':40}
common_pairs = dict()
# for x in dict1:
#     if (x in dict2 and dict1[x] == dict2[x]):
#         common_pairs[x] = dict1[x]+dict2[x]
#         print(common_pairs)
a = dict()
if len(dict1) > len(dict2):
    for x in dict1:
        if (x not in dict2):
            a[x] = dict1[x]
    print(a)            
else:
    for x in dict2:
        if (x not in dict1):
            a[x] = dict2[x]            
    print(a)


    
    
    
    
d1 = {'a': 10, 'c':20, 'd':30, 'e':40}

d2 = {'a': 10, 'b':20, 'c':30}

d3 = {}

for i, j in d1.items():

    for x, y in d2.items():

        if i == x:

            d3[i]=(j+y)

print(d3)    










#=============================================

dict1 = {'a': 10, 'b':20, 'c':30}
dict2 = {'a': 10, 'c':20, 'd':30, 'e':40}
dict3 = {}
for x,y in dict1.items():
    for a,b in dict2.items():
        if x == a:
            dict3[x] = (y+b) 
a = dict()
if len(dict1) > len(dict2):
    for x in dict1:
        if (x not in dict2):
            a[x] = dict1[x]            
else:
    for x in dict2:
        if (x not in dict1):
            a[x] = dict2[x]            
dict3.update(a)
print(dict3)
dict4 = {}
for c,d in dict1.items():
    for e,f in dict3.items():
        if c not in e:
            dict4 = c
print(dict4)   
