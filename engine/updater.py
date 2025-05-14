import pandas as pd
from datetime import datetime
import streamlit as st

LOCAL_CSV_PATH = "data/consolidated-list.csv"

def fetch_and_update_if_needed(conn):
    df = pd.read_csv(LOCAL_CSV_PATH, sep=';', encoding='utf-8', engine='python')


    st.write("Colonnes disponibles :", list(df.columns))  # Debug temporaire

    df = df[['NameAlias_WholeName', 'RegimeName']]
    df.columns = ['name', 'program']
    df['updated_at'] = datetime.utcnow().isoformat()

    df.to_sql('sanctions', conn, if_exists='replace', index=False)

    return df
