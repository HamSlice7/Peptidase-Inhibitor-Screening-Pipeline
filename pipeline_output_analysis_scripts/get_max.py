import pandas as pd
import sys

data = sys.argv[1]
metric = str(sys.argv[2])
df = pd.read_csv(data)

def get_max(df: pd.DataFrame, metric:str) -> pd.DataFrame:

    """
    Return a data frame of the max values for chosen metric (ipTM, LIS, LIA)

    Parameters:
        - csv_file (pd.DataFrame): path to a csv file with labels of 1 for a positive PPI and 0 for a negative PPI for each complex

    Return:
        - Max metric of choice for each complex
    """


    #Group the pipeline data by "Protein 1" and "Protein 2" and then take the max of the groups based on the specified "metric"
    df_complex_max = df.groupby(["Protein 1", "Protein 2"])[metric].max().reset_index()
    df_binary_label = df.groupby(["Protein 1", "Protein 2"])["Binary_Label"].mean().reset_index()

    final_df = pd.concat([df_complex_max, df_binary_label["Binary_Label"]], axis = 1)

    final_df.to_csv(f"..\output\mean_max\{metric}_max.csv", index=False)
        


get_max(df, metric)