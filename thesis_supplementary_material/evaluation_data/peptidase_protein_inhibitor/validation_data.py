import pandas as pd
import random
import sys

random.seed(25)

input_df = sys.argv[1]

df_positive = pd.read_csv(input_df)


#make a copy of df_positive which will be used to make a negative control
df_negative = df_positive

#create a new negative control data frame
inhibitor_families = df_negative['Inhibitor Family'].unique()

random_pairs = []
count = 0

while count < df_negative.shape[0]:
    peptidase = df_negative['Peptidase'][count]
    peptidase_family = df_negative['Peptidase Family'][count]
    inhibtor_family = random.choice([fam for fam in inhibitor_families if fam != peptidase_family])
    inhibitor = random.choice(df_negative[df_negative['Inhibitor Family'] == inhibtor_family]['Inhibitor'].to_list())
    new_pair = {'Peptidase': peptidase, 'Peptidase Family':peptidase_family, 'Inhibitor':inhibitor, 'Inhibitor Family':inhibtor_family}
    if new_pair not in random_pairs:
        random_pairs.append(new_pair)
        count += 1
    else:
        pass

df_negative = pd.DataFrame(random_pairs) 

df_validation_final = pd.concat([df_positive,df_negative],ignore_index=True, axis = 0)
df_validation_final.to_csv("df_validation_final.csv", index = False)
