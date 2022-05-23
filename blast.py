from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("../Section1/Chap8/buccal_swab.unmapped1.fasta",format = "fasta")
handle = NCBIWWW.qblast("blastn","nt",record.format("fasta"))

result = handle.readlines()
for s in result:
    print(s)
