from typing_extensions import _SpecialForm


dic={"a":50,"b":60,"c":58,"d":56,"e":40,"f":100,"g":20}
m=0
sm=0
tm=0
b={ }
for x in dic:
    if dic[x]>max:
        sm=m
        m=dic[x]
    if sm<dic[x] and dic[x]<m:
        sm=dic[x]
    if dic[x]<m and dic[x]>tm:
        tm=dic[x]
    b["e"]=m
    b["b"]=sm
    b["c"]=tm
b.update()
print(b)