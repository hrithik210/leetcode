import pandas as pd

def fix_names(df: pd.DataFrame) -> pd.DataFrame:
    df['name'] = df['name'].str.capitalize()
    df = df.sort_values(by='user_id' , ascending=True)
    return df