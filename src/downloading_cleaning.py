def import_clean (dataset_loc):
    """
    Takes a dataset in csv format and returns a pandas object without blank lines and duplicates
    """
    import pandas as pd
    df = pd.read_csv(dataset_loc, low_memory=False)
    print(f"""
    Before Cleaning:
    Rows: {df.shape[0]}
    Columns: {df.shape[1]}
    """)
    df.dropna(how="all", inplace=True)
    df = df.drop_duplicates()
    print(f"""
    After Cleaning:
    Rows: {df.shape[0]}
    Columns: {df.shape[1]}
    """)
    return df
def col_clean (df):
    df2 = df[['']]
    return df2