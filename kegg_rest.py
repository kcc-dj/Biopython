from Bio.KEGG import REST

hpath=REST.kegg_list("pathway","hsa").read()

insulin_path=[]

for line in hpath.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "insulin" in description.lower():
        insulin_path.append(entry)
        print(entry,description)

print(insulin_path)

insulin_genes = []

for path in insulin_path:
    path_file=REST.kegg_get(path).read()

    current_section = None
    for line in path_file.rstrip().split("\n"):
        section = line[:12].strip()
        print(section)
        if not section=="":
            current_section = section
            if current_section=="GENE":
                gene_identifiers,gene_description = line[12:].split("; ")
                gene_id,gene_symbol=gene_identifiers.split()
                if not gene_symbol in insulin_genes:
                    insulin_genes.append(gene_symbol)


print(",".join(insulin_genes))
