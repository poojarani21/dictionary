dict={"a":" muskan","b":[1,2,3],"c":[5,6,7]}
for i in dict.values():
    if type(i)==list:
        j=0
        while j<len(i):
            print(i[j])
            if j==1:
                break
            j+=1
    else:
        print(i)