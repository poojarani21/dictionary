dict={"alex":["subj1","subji2","subji3"],"david":["subji4","subji5"]}
b=[]
count=0
for x in dict:
    b.append (dict[x])
    for i in b:
        count=count+len(b)
print(count)
