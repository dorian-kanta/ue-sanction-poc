import pandas as pd
from datetime import datetime
import streamlit as st

LOCAL_CSV_PATH = "data/consolidated-list.csv"

def fetch_and_update_if_needed(conn):
    df = pd.read_csv(LOCAL_CSV_PATH, sep=';', encoding='utf-8', engine='python')

    st.text("Colonnes disponibles :")
    st.write(df.columns.tolist())

    df = df[['NameAlias_WholeName', 'Entity_Regulation_Programme']].dropna()
    df.columns = ['name', 'program']
    df['updated_at'] = datetime.utcnow().isoformat()
    df.to_sql('sanctions', conn, if_exists='replace', index=False)

    return df
