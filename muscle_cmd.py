from Bio.Align.Applications import MuscleCommandline

muscle_exe = "/home/djkim/practice_biopython/biopython-master/muscle5.1.linux_intel64"

cmd_line = MuscleCommandline(muscle_exe,input="../Section1/Chap7/HBA.all.fasta", out = "HBA.aln", clw=" ")

print(cmd_line)

stdout, stderr = cmd_line()
