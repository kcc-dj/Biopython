from Bio import Entrez

Entrez.email="kcc0225@naver.com"

aa=Entrez.esearch(db="pubmed",term="bioinformatics")
bb=Entrez.read(aa)
print(bb["Count"])
