dic={"name":"puja","age":25,"salary":8000,"city":"newyork"}
k=["name","salary"]
d={}
i=0
while i<len(k):
    if k[i] in dic:
        j=(k[i])
        d.update(j)
        i=i+1
    print(d)