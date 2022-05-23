from Bio import Entrez

Entrez.email="kcc0225@naver.com"
aa=Entrez.efetch(db="nucleotide",id="NC_001498",rettype="gb",retmode="xml")
bb=Entrez.read(aa)
for i in bb:
    print(i["GBSeq_locus"])
    print(i["GBSeq_definition"])
