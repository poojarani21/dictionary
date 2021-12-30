d ={'1':['a','b'], '2':['c','d']}
a=d["1"]
b=d["2"]
i=0
while i<len(a):
    j=0
    while j<len(b):
        print(a[i],b[j])
        j=j+1
    i=i+1