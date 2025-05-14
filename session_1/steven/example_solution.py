import pandas as pd
from typing import List, Literal

def read_csv_data(
        file_prefix: str, 
        filename: str
    ) -> pd.DataFrame:
    return pd.read_csv(f"{file_prefix}{filename}")

def drop_na_from_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def convert_date_cols(
        df: pd.DataFrame, 
        date_cols: List[str]
    ) -> pd.DataFrame:
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])
    return df

def calculate_summary_stats(
        df: pd.DataFrame, 
        category_column_name: str, 
        value_column_name: str, 
        summary: Literal["mean", "median"]
    ) -> pd.DataFrame:
    if summary == "mean":
        return df.groupby(category_column_name)[value_column_name].mean().reset_index()
    elif summary == "median":
        return df.groupby(category_column_name)[value_column_name].median().reset_index()

def output_csv(
        df: pd.DataFrame, 
        export_path: str
    ) -> None:
    df.to_csv(export_path, index=False)

def main(
        file_prefix: str, 
        filename: str, 
        date_cols: List[str], 
        category_column_name: str, 
        value_column_name: str, 
        summary: Literal["mean", "median"], 
        export_path: str
    ) -> None:
    df = read_csv_data(file_prefix, filename)
    df = drop_na_from_df(df)
    df = convert_date_cols(df, date_cols)
    df = calculate_summary_stats(df, category_column_name, value_column_name, summary)
    output_csv(df, export_path)

if __name__ == "__main__":
    main()