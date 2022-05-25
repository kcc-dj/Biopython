aa=['A','C','G','T']
bb=['A','C','G','T']
def kmer(num,a1,b1):
    
    if num==1:
        print(b1)
        print(len(b1))
    else:
        cc=list()
        for i in a1:
            for j in b1:
                cc.append(i+j)
        b1=cc
        num-=1
        return(kmer(num,a1,b1))

kmer(3,aa,bb)



