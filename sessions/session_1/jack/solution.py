from functools import wraps
import pandas as pd

def read_csv(
        file_name: str
    ) -> pd.DataFrame:
    file_name_prefix = "input/"
    if not file_name.startswith(file_name_prefix):
        file_name = f"{file_name_prefix}{file_name}"

    try:
        return pd.read_csv(file_name) 
    except:
        raise ValueError(
            f"Unable to read in the file located at, {file_name}, please check it is a csv and is in the correct directory"
        )

class ColumnNames:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

def write_summary(func):
    @wraps(func)
    def wrapper(dataframe, column_names, output_path):
        df = dataframe.dropna()
        df[column_names.date] = pd.to_datetime(df[column_names.date])
        summary: pd.Series = func(df, column_names)
        summary.to_csv(output_path)
    return wrapper

@write_summary
def mean_summary(
        dataframe: pd.DataFrame,
        column_names: ColumnNames,
    ) -> pd.Series:
    summary = dataframe.groupby(column_names.category)[column_names.value].mean()
    return summary

@write_summary
def median_summary(
        dataframe: pd.DataFrame,
        column_names: ColumnNames
    ) -> pd.Series:
    summary = dataframe.groupby(column_names.category)[column_names.value].median()
    return summary

def main(
    file_path: str,
    output_path: str,
    col_names: dict
):
    df = read_csv(file_path)
    mean_summary(df, col_names, output_path)

if __name__ == "__main__":
    main()