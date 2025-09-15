import pandas as pd

def extract_csv(filepath: str):
    df = pd.read_csv(filepath)
    return df

    