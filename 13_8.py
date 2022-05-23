from Bio import ExPASy, SwissProt

acc = "P04637"
handle = ExPASy.get_sprot_raw(acc)
record = SwissProt.read(handle)
print(record.gene_name)
print(record.organism)
print(record.sequence)
