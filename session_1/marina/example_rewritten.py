import pandas as pd

def process_data(filename, file_nameprefix, date_columns_name, category_column_name, value_column_name):
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


def load_data(filename:str, file_nameprefix:str):
    return pd.read_csv(f"{file_nameprefix}{filename}")

def clean_format_data(df:pd.DataFrame, date_columns_name: list[str]):
    df = df.dropna()
    df[date_columns_name] = pd.to_datetime(df[date_columns_name])
    return df

#def compute_summary(df:pd.DataFrame, category_column_name:str, value_column_name: str, summary:str)