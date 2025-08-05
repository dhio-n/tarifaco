# Criar coluna para pesquisa concatenando todas as colunas
df['search_field'] = df.astype(str).agg(' '.join, axis=1)

search_term = st.text_input("🔍 Pesquisar na tabela:")

if search_term:
    filtered_df = df[df['search_field'].str.contains(search_term, case=False, na=False)]
    st.write(f"🔎 {len(filtered_df)} resultado(s) para: **{search_term}**")
    st.dataframe(filtered_df.drop(columns=['search_field']), use_container_width=True)
else:
    st.dataframe(df.drop(columns=['search_field']), use_container_width=True)
