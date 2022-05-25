s1="ACACA"
s2="ATTCA"

def palin(ch):
    aa=0
    for i in range(len(ch)):
        if ch[i]!=ch[-i-1]:
            print("False")
            break
        else:
            aa+=1
        if aa==len(ch)//2:
            print("True")
            break

palin(s1)
palin(s2)
