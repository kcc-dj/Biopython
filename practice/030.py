seq = "AGTTTATAG"
aa=""
for i in range(len(seq)):
    if seq[i]=="A":
        aa+=("T")
    elif seq[i]=="C":
        aa+=("G")
    elif seq[i]=="G":
        aa+=("C")
    else :
        aa+=("A")

print(aa)
