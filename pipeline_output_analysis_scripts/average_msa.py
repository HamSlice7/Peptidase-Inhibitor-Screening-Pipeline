import pandas as pd
import sys

average_peptide_inhibitors_file = sys.argv[1]
df = pd.read_csv(average_peptide_inhibitors_file)


df_TP = df[df['Binary_Label'] == 1]

#Subsetting based on the index of unique rows in P2 column
df_TP_removed_duplicates_P2 =  df_TP.loc[df_TP['Protein 2'].drop_duplicates().index]

print(df_TP_removed_duplicates_P2['MSA_depth_inhibitors'].mean())