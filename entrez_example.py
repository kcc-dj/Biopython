from Bio import Entrez

Entrez.email = "kcc0225@naver.com"

handle = Entrez.efetch(db="nucleotide",rettype="gb",id="AY463215",retmode="text")

for s in handle:
    print(s.strip())
