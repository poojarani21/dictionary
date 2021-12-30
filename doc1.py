d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
dic={}
for x in d1.keys():
    for y in d2.keys():
        if x==y:
            dic[x]=d1[x]+d2[y]
else:
    dic[x]=d1[x]
    dic[y]=d2[y]
print(dic)




# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# for x in dic1.keys():
#     for y in dic2.keys():
#         for z in dic3.keys():
#             if x==y or y==z or x==z:
#                 dic4[x]=dic1[x]+dic2[y]+dic3[z]
# else:
#     dic4[x]=dic1[x]
#     dic4[y]=dic2[y]
#     dic4[z]=dic3[z]
# print(dic4)