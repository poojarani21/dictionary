a="MISSISSIPPI"
i=0
b={ }
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
            b[a[i]]=count
        j=j+1
print(b)