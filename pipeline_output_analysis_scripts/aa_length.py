from Bio import SeqIO
import sys
import pandas as pd

fasta_file = sys.argv[1]


id = []
aa_length = []

for record in SeqIO.parse(fasta_file, "fasta"):
    id.append(record.id)
    aa_length.append(len(record.seq))


id_aa_length = {"ID":id, "AA_Length":aa_length}


df_aa_length = pd.DataFrame(id_aa_length)

df_aa_length.to_csv("aa_length.csv", index=False)

##subset inhibitors
df_aa_length_inhibitors = df_aa_length[df_aa_length["ID"].str.islower()]

df_aa_length_inhibitors.to_csv("aa_length_inhibitors.csv", index=False)

