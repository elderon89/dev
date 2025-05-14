# Recarregando os dados com os parâmetros corretos novamente
df1 = pd.read_csv(file_1, encoding='ISO-8859-1', sep=';')
df2 = pd.read_csv(file_2, encoding='ISO-8859-1', sep=';')
df3 = pd.read_csv(file_3, encoding='ISO-8859-1', sep=';')

# Selecionar colunas relevantes para comparação
precos_df1 = df1[['Codigo', 'Valor']].rename(columns={'Valor': 'Valor_14052025_1635'})
precos_df2 = df2[['Codigo', 'Valor']].rename(columns={'Valor': 'Valor_05022025_1335'})
precos_df3 = df3[['Codigo', 'Valor']].rename(columns={'Valor': 'Valor_14052025_1430'})

# Comparações 2 a 2
comparacao_1_2 = precos_df1.merge(precos_df2, on='Codigo', how='inner')
comparacao_1_3 = precos_df1.merge(precos_df3, on='Codigo', how='inner')
comparacao_2_3 = precos_df2.merge(precos_df3, on='Codigo', how='inner')

# Mostrar as primeiras linhas das comparações
comparacao_1_2.head(10), comparacao_1_3.head(10), comparacao_2_3.head(10)
