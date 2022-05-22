from Bio import Entrez,SeqIO

Entrez.email = "kcc0225@naver.com"

with  Entrez.efetch(db="nucleotide",rettype="fasta",id="42540826",retmode="text") as handle:
    seq = SeqIO.read(handle,"fasta")


print(seq)
print(len(seq))
