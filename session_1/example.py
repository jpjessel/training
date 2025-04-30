import pandas as pd

def process_data(
        filename, 
        file_nameprefix, 
        date_columns_name, 
        category_column_name, 
        value_column_name
    ):
    
    df = pd.read_csv(file_nameprefix + filename)

    df = df.dropna()
    df[date_columns_name] = pd.to_datetime(df[date_columns_name])
    
    if summary == "mean":
        summary = df.groupby(category_column_name)[value_column_name].mean()
    elif summary == "median":
        summary = df.groupby(category_column_name)[value_column_name].median()

    print("Summary Stats:")
    print(summary)

    summary.to_csv("output/summary.csv")

def main(file_path):
    process_data(file_path)

if __name__ == "__main__":
    main()