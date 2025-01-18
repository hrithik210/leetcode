import pandas as pd

def find_patients(df: pd.DataFrame) -> pd.DataFrame:
    df1 = df.loc[df['conditions'].str.contains(r'\bDIAB1'), ['patient_id' , 'patient_name' , 'conditions']]
    return df1