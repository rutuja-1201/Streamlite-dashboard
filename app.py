import streamlit as st
import pandas as pd

df = pd.read_csv('data/github_dataset.csv')
st.write(df.head())


top_repos = df.sort_values(by='stars_count', ascending=False).head(10)


st.subheader('Top 10 Repositories by Stars')
st.bar_chart(top_repos[['repositories', 'stars_count']].set_index('repositories'))
