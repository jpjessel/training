from sessions.session_1.jack.solution import read_csv, mean_summary, ColumnNames

def run():
    col_names = ColumnNames(
        id = "id",
        date="date",
        category="category",
        value="value"
    )

    df = read_csv("data.csv")

    mean_summary(
        df,
        col_names,
        "output/mean.csv"
    )

if __name__ == "__main__":
    run()