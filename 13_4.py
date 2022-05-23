from Bio import SeqIO

aa=SeqIO.read("../Section1/Chap13/NM_000384.2.gb","genbank")
print(aa.id)
print(aa.description)
print(aa.annotations["molecule_type"])
print(aa.annotations["organism"])
