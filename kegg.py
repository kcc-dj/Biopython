from Bio.KEGG import Enzyme

records = Enzyme.parse(open("../Section1/Chap12/ec_2.7.1.40.txt"))
record=list(records)[0]
#print(record.classname)
#print(record.sysname)
#print(record.substrate)
#print(record.product)
