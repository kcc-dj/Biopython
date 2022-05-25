seq="MLSSSMPPGGLACHADDDII"
aa=dict()

for i in seq:
    if i in aa:
        aa[i]+=1
    else:
        aa[i]=1

print(aa)
bb=sorted(aa.items(),key=lambda j : j[1] )
print(bb)



