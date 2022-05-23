from Bio.Blast import NCBIWWW
from Bio import SeqIO

aa=SeqIO.read("../Section1/Chap13/13.6.fasta","fasta")
bb=NCBIWWW.qblast("blastn","nt",aa.format("fasta"))
result=bb.readlines()
for i in result:
    print(i)
