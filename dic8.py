data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d={}
for i in data.values():
    if data[i] not in d:
        d[i]=data[i]
print(d)
