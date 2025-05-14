# 🇪🇺 Kanta KYC – Liste de sanctions UE

Petite application Streamlit pour vérifier si une personne ou entité est présente sur la liste des sanctions de l'Union Européenne.

---

## 🚀 Fonctionnalités
- Vérification d'un nom via fuzzy matching (tolérant aux fautes)
- Mise à jour automatique depuis un fichier `.csv` local structuré
- Affichage de la date de dernière mise à jour
- Stack légère : Streamlit + SQLite + pandas + RapidFuzz

---

## 📁 Arborescence

```
kanta_kyc_sanctions/
├── app.py                        # App Streamlit principale
├── engine/
│   ├── matcher.py               # Moteur de fuzzy match
│   └── updater.py               # Chargement et parsing du CSV
├── db/
│   ├── database.py              # Connexion + schéma + accès DB
├── data/
│   └── consolidated-list.csv   # Liste des sanctions (source CSV locale)
│   └── sanctions.sqlite        # Base générée automatiquement
├── requirements.txt
├── README.md
```

---

## 🛠 Installation

```bash
pip install -r requirements.txt
mkdir -p data
cp ton_fichier.csv data/consolidated-list.csv
streamlit run app.py
```

---

## 📝 Format CSV attendu
Le fichier `.csv` doit contenir au moins les colonnes :
- `NameAlias_WholeName`
- `Entity_Regulation_Programme`

Ces champs seront renommés en `name` et `program` dans la base SQLite.

---

## 📌 À venir ?
- Upload de fichiers CSV depuis l'UI
- Requête API avec FastAPI (mode service)
- Ajout de logs d’audit / historique

---

Made with ❤️ chez Kanta