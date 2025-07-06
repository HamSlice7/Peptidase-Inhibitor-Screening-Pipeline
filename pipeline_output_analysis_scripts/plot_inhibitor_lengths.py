import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys

data = sys.argv[1]

df = pd.read_csv(data)


sns.histplot(data = df, x = "AA_Length", discrete=True)

# Add labels and title
plt.xlabel('Amino Acid Lengths of Inhibitors')
plt.ylabel('Count')
#plt.title(f'Distribution of Max {metric}')

plt.show()