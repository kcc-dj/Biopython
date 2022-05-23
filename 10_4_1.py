from Bio import ExPASy,SwissProt

acc="P05067"
aa=ExPASy.get_sprot_raw(acc)
bb=SwissProt.read(aa)
print(bb.description)
print(bb.gene_name)
print(bb.organism)
print(bb.sequence_length)
print(bb.sequence)
