# Load Packages
import pandas as pd
from typing import List

# Create function to load in data 
def load_data(filename: str, filename_prefix: str): 
    # Load in data with the corresponding prefix and filename
    df = pd.read_csv(filename_prefix + filename)  
    return df

def process_data_columns(df:pd.DataFrame, date_columns_name: [str]): 
    # Drop all NA's from the data 
    df_cleaned = df.dropna()
    # Set Date Columns to date_time
    df_cleaned[date_columns_name] = pd.to_datetime(df_cleaned[date_columns_name])

    return df_cleaned

def obtain_summary_statistics(category_column_name: str, value_column_name: str): 
    # Set value to numeric to ensure that we can obtain summary statistics 
    df_cleaned[category_column_name] = pd.to_numeric(df_cleaned[category_column_name])

    # Create if else statement to set what the output should be based on the input
    if summary == "mean": 
        summary = df_cleaned.groupby(category_column_name)[value_column_name].mean() 
    elif summary == "median": 
        summary = df_cleaned.groupby(category_column_name)[value_column_name].median() 
    print("Summary Stats:")
    print(summary) 

# @ -- decorator: defines function and can define two summary functions 
# extend original functions purpose using decorator function 

# def process_data(filename, file_nameprefix, date_columns_name, category_column_name, value_column_name):
#    df = pd.read_csv(file_nameprefix + filename)

#    df = df.dropna()
#    df[date_columns_name] = pd.to_datetime(df[date_columns_name])
   
#    if summary == "mean":
#        summary = df.groupby(category_column_name)[value_column_name].mean()
#    elif summary == "median":
#        summary = df.groupby(category_column_name)[value_column_name].median()

#    print("Summary Stats:")
#    print(summary)

#    summary.to_csv("output/summary.csv")

# def main(file_path):
#    process_data(file_path)

if __name__ == "__main__":
    main()