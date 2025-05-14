import streamlit as st
from engine.matcher import fuzzy_match_name
from engine.updater import fetch_and_update_if_needed
from db.database import init_db, get_all_sanctions

st.title("KYC ⚖️ - Vérification liste de sanctions UE")

name_input = st.text_input("Nom à vérifier")

if st.button("Vérifier") and name_input:
    conn = init_db()
    df = get_all_sanctions(conn)

    result, score = fuzzy_match_name(name_input, df)
    if result and score >= 90:
        st.error(f"❌ Potentiellement listé : **{result}** (score {score})")
    else:
        st.info("Nom non trouvé localement, interrogation de la source officielle...")
        df = fetch_and_update_if_needed(conn)
        result, score = fuzzy_match_name(name_input, df)
        if result and score >= 90:
            st.error(f"❌ Trouvé dans la liste UE : **{result}** (score {score})")
        else:
            st.success("✅ Aucun match détecté")
    conn.close()
