from Bio import AlignIO

align = AlignIO.read("../Section1/Chap7/example.aln","clustal")
for record in align:
    print("%s - %s" % (record.seq,record.id))
