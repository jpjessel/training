from datetime import datetime
import pandas as pd

schemas_and_columns = {
    'england': {
        'schema': {
            'DATE': datetime,
            'REGION_CODE': str,
            'REGION_NAME': str,
            'SEX': str,
            'COVERAGE_PERCENT': float,
        },
        'col_names': {
            'Date': 'DATE',
            'Area Code': 'REGION_CODE',
            'Area Name': 'REGION_NAME',
            'Sex': 'SEX',
            'Value': 'COVERAGE_PERCENT'
        }
    },
    'imd': {
        'schema': {
            'DATE': datetime,
            'REGION_CODE': str,
            'REGION_NAME': str,
            'SEX': str,
            'IMD_DECILE': int,
            'COVERAGE_PERCENT': float,
        },
        'col_names': {
            'Date': 'DATE',
            'Area Code': 'REGION_CODE',
            'Area Name': 'REGION_NAME',
            'Sex': 'SEX',
            'Category': 'IMD_DECILE',
            'Value': 'COVERAGE_PERCENT'
        }
    }
}

df = pd.read_csv("input.csv")
source_max_date = df["Date"].max()

df_hist = pd.read_csv("history.csv")
hist_max_date = df_hist["DATE"].max()

if source_max_date <= hist_max_date:
    raise ValueError("No new data.")

for key, value in schemas_and_columns.items():

    if key == 'england':
        df_processed = df[
            (df['Area Name'].str.lower() == "england") 
            & df['Category'].isnull()
        ]

    elif key == 'imd':
        df_processed = df[
            (df['Area Type'].str.lower() == "all".lower()) &
            df['Category'].notnull()
        ]
        
    df_processed: pd.DataFrame = df.rename(columns={c: value['col_names'].get(c, c) for c in df.columns})

    processed_columns = list(value['schema'].keys())
    df_processed = df_processed[processed_columns]

    for col, dtype in value['schema'].items():
        df_processed[col] = df_processed[col].astype(dtype)

    df_processed['DATA_INGESTED'] = pd.to_datetime('today').normalize()

    df_processed.to_excel("output.csv")