seq="MLSSSMPPGGLACHADDDII"
aa=dict()

for i in seq:
    if i in aa:
        aa[i]+=1
    else:
        aa[i]=1

print(aa)
for j in aa:
    print(aa[j])

