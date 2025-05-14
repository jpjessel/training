from config import SchemaAndColumns

from functools import wraps
from typing import Tuple
from datetime import datetime, date
import pandas as pd

def read_source(
        file_name: str
    ) -> Tuple[pd.DataFrame, date]:

    df = pd.read_csv(f"input/{file_name}")
    source_max_date = pd.to_datetime(df["Date"]).max()
    return df, source_max_date

def read_sink(
        file_name: str
    ) -> Tuple[pd.DataFrame, date]:

    df_hist = pd.read_csv(f"input/{file_name}")

    hist_max_date = pd.to_datetime(df_hist["DATE"]).max()

    return df_hist, hist_max_date

def processing_decorator(filter_func):
    def wrapper(
            config_file: SchemaAndColumns, 
            filter: str
        ) -> pd.DataFrame:
        source_df, source_date = read_source(config_file.source_file)
        _, target_date = read_sink(config_file.target_file)

        if source_date <= target_date:
            raise ValueError("No new data.")

        schema = config_file.create_schema(filter)
        column_map = config_file.create_column_map(filter)

        df_filtered = filter_func(source_df)
        df_renamed = df_filtered.rename(columns=column_map)
        df_selected = df_renamed[list(schema.keys())]
        df_typed = df_selected.astype(schema)
        df_typed['DATA_INGESTED'] = pd.to_datetime('today').normalize()

        return df_typed

    return wrapper

@processing_decorator
def bowel_cancer_england(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
    df_filtered = dataframe[
        (dataframe['Area Name'].str.lower() == "england") 
        & dataframe['Category'].isnull()
    ]
    return df_filtered

@processing_decorator
def bowel_cancer_imd(
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
    
    df_filtered = dataframe[
        (dataframe['Area Name'].str.lower() == "area 1".lower()) &
        dataframe['Category'].notnull()
    ]
    return df_filtered