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

