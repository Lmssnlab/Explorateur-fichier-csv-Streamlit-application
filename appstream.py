import streamlit as st
import pandas as pd

# Permettre à l'utilisateur de télécharger un fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

# Vérifier si un fichier a été téléchargé
if uploaded_file is not None:
    # Lire le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv(uploaded_file)
    
    # Obtenir le nombre de lignes
    num_lignes = len(df)
    
    # Obtenir le volume (taille en octets)
    volume = uploaded_file.getvalue().__sizeof__()
    
    # Obtenir le nombre de colonnes
    num_colonnes = len(df.columns)
    
    # Afficher les informations
    st.write(f"Nombre de lignes : {num_lignes}")
    st.write(f"Volume : {volume} octets")
    st.write(f"Nombre de colonnes : {num_colonnes}")
    
    # Afficher les premières lignes du DataFrame
    st.write(df.head())
else:
    st.warning("Veuillez télécharger un fichier CSV.")