from Bio import ExPASy,SwissProt

accession="P02649"
aa=ExPASy.get_sprot_raw(accession)
bb=SwissProt.read(aa)
print(bb.gene_name)
print(bb.organism)
print(bb.sequence_length)
print(bb.sequence)
