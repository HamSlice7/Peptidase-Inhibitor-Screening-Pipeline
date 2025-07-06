import pandas as pd
import sys

data = sys.argv[1]
df = pd.read_csv(data)

def get_sd(data: pd.DataFrame) -> pd.DataFrame:

    """
    Return a data frame of the standard deviation for ipTM, LIS, LIA, pTM, AF Confidience (0.8*ipTM + 0.2*pTM)
    and pLDDT from the 5 predicted structure for each complex

    Parameters:
        - csv_file (pd.DataFrame): path to a csv file with labels of 1 for a positive PPI and 0 for a negative PPI for each complex

    Return:
        - SD of ipTM, LIS, LIA, pTM, AF Confidience (0.8*ipTM + 0.2*pTM)
          and pLDDT values from each complex.

    """

    #assign the pipeline output data to the variable 'df'
    df = data

    #Create a list of the metrics that will be used for averages
    metric_columns = ["LIS", "LIA", "ipTM", "pTM", "AFM Confidence", "pLDDT"]


    #Group the pipeline data by "Protein 1" and "Protein 2" and then take the means of the groups based on the specified columns in the "metric_columns" list
    df_complex_sd = df.groupby(["Protein 1", "Protein 2"])[metric_columns].std().reset_index()
    df_complex_label = df.groupby(["Protein 1", "Protein 2"])["Binary_Label"].mean().reset_index()

    df_complex_sd_final = pd.concat([df_complex_sd, df_complex_label], axis = 1)

    df_complex_sd_final.to_csv("..\output\mean_max\std.csv", index=False)

    return df_complex_sd

get_sd(df)