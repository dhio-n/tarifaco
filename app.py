import streamlit as st
import pandas as pd
import os

CSV_PATH = "tabela_whitehouse_traduzida.csv"

st.set_page_config(page_title="Tarifaço: Brasil 🇧🇷 vs EUA 🇺🇸", layout="wide")

# Título e cabeçalho
st.header("Tarifaço: Itens que **não vão ser taxados** 🇧🇷 vs 🇺🇸")
st.subheader("🔎 O que não será tarifado e por quê?")

# Introdução
st.markdown("""
Imagine um 'tarifaço' — um aumento abrupto de **50% em tarifas** sobre produtos brasileiros entrando nos Estados Unidos 🇺🇸.  
Apesar do impacto ser grande, **quase 700 itens foram EXCLUÍDOS do aumento**, incluindo setores estratégicos como aviação civil (Embraer), energia, minérios e sucos cítricos.  
A medida, anunciada por Trump e implementada em **1º de agosto de 2025**, teve como justificativa alegações de ameaças à segurança nacional e interferência política brasileira.  
Por outro lado, o Brasil reagiu com protestos populares (o movimento nas redes ficou conhecido como *vampetaço*) e buscou negociações diplomáticas intensas, além de apoio da OMC.

A tabela abaixo foi publicada oficialmente pela Casa Branca com os códigos HTSUS e descrição dos produtos **não afetados pelo tarifaço**.

🔗 **Fonte oficial da tabela**: [White House – Addressing Threats to the US](https://www.whitehouse.gov/presidential-actions/2025/07/addressing-threats-to-the-us/)
""")

# Verifica se o CSV existe
if not os.path.exists(CSV_PATH):
    st.warning("O arquivo CSV ainda não foi gerado. Rode o script localmente ou use o GitHub Actions para atualizar.")
else:
    df = pd.read_csv(CSV_PATH)
    search_term = st.text_input("🔍 Pesquisar na tabela:")

if search_term:
    # Converte todas as colunas para string e verifica se algum valor contém o termo (case-insensitive)
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]

    st.write(f"🔎 {len(filtered_df)} resultado(s) para: **{search_term}**")
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
