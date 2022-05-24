seq = "AGTTTATAG"
aa=""
for i in seq[::-1]:
    if i=="A":
        aa+=("T")
    elif i=="C":
        aa+=("G")
    elif i=="G":
        aa+=("C")
    else :
        aa+=("A")
print(seq)
print(aa)
