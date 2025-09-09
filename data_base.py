import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
import numpy as np


# Título da Dashboard
st.title('Análise de Avaliações de Produtos')
st.markdown('---')

# 1. Carregamento dos Dados do SQLite
@st.cache_data
def load_data(db_file):
    """Carrega os dados do banco de dados SQLite."""
    engine = create_engine(f'sqlite:///{db_file}')
    query = "SELECT * FROM reviews;"
    df = pd.read_sql(query, con=engine)
    return df

df = load_data('./database.sqlite')
df = df.sample(n=50000, random_state=42)

st.header('Visão Geral dos Dados')
st.write(f"O dataset possui **{df.shape[0]}** linhas e **{df.shape[1]}** colunas.")
st.write("Primeiras 5 linhas do DataFrame:")
st.dataframe(df.head())
st.markdown('---')

# 2. Limpeza dos Dados
df.dropna(subset=['Text', 'Score'], inplace=True)
df.drop_duplicates(inplace=True)
st.write(f"Após a limpeza, o dataset tem **{df.shape[0]}** linhas.")
st.markdown('---')

# 3. Gráfico 1: Distribuição das Notas
st.header('Distribuição das Notas dos Produtos')
score_counts = df['Score'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=score_counts.index, y=score_counts.values, ax=ax)
ax.set_title('Distribuição das Notas dos Produtos')
ax.set_xlabel('Nota (Score)')
ax.set_ylabel('Número de Avaliações')
st.pyplot(fig)
st.markdown('---')

# 4. Análise de Sentimento
st.header('Análise de Sentimento das Avaliações')
@st.cache_resource
def download_nltk_data():
    """Baixa o lexicon do NLTK."""
    nltk.download('vader_lexicon', quiet=True)
download_nltk_data()

analyser = SentimentIntensityAnalyzer()
df['Sentimento'] = ''
total_linhas = len(df)
progress_bar = st.progress(0)

for i, row in df.iterrows():
    text = str(row['Text'])
    score = analyser.polarity_scores(text)
    if score['compound'] >= 0.05:
        df.loc[i, 'Sentimento'] = 'Positivo'
    elif score['compound'] <= -0.05:
        df.loc[i, 'Sentimento'] = 'Negativo'
    else:
        df.loc[i, 'Sentimento'] = 'Neutro'

    progress_bar.progress(int((i + 1) / total_linhas))

progress_bar.progress(1.0)
st.success('Análise de sentimento concluída!')

st.header('Contagem de Sentimentos (Diagnóstico)')
st.write(df['Sentimento'].value_counts())
st.markdown('---')

# 5. Gráfico 2: Distribuição de Sentimento

st.header('Distribuição de Sentimento')
sentimento_counts = df['Sentimento'].value_counts()
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(x='Sentimento', data=df, ax=ax)
ax.set_title('Distribuição de Sentimento das Avaliações')
st.pyplot(fig)

st.success("Análise completa! Veja os resultados abaixo.")