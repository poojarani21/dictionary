dict={"a":51,"b":22,"c":333,"d":44}
list=[]
maxi=0
sec=0
third=0
for i in dict:
    if dict[i]>maxi:
        sec=maxi
        maxi=dict[i]
    if sec<dict[i]<maxi:
        third=sec
        sec=dict[i]
    if third<sec>dict[i]<maxi:
        third=dict[i]
print(maxi)
print(sec)
print(third)
s=third,sec,maxi
list.append(s)
print(list)