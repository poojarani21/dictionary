dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
d={}
for i in dict.keys():
    if bool(dict[i])==True:
        d[i]=dict[i]
print(d)
        