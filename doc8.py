x={"1":2,"3":4,"5":6,"7":8}
y=input("enter somrthing")
i=0
while i<len(x):
    if y in x:
        print("exist")
        break
    else:
        print("not exist")
    i=i+1