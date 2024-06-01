import streamlit as st
import pandas as pd

df = pd.read_excel ('static/datasets/compudata.xlsx')

st.table (df.head(10))