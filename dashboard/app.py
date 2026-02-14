import streamlit as st
import pandas as pd

# Load cleaned data (or raw and clean inline)
df = pd.read_csv('data/raw/student-mat.csv')

# Basic cleaning
df = df.drop_duplicates()
df.columns = df.columns.str.lower().str.replace(" ", "_")
df['final_grade'] = (df['g1'] + df['g2'] + df['g3']) / 3
df['at_risk'] = df['final_grade'] < 10

# Dashboard UI
st.title("University Student Insights Dashboard")
st.metric("Average Final Grade", round(df['final_grade'].mean(), 2))
st.metric("At Risk Students (%)", round(df['at_risk'].mean() * 100, 2))

st.subheader("Absences vs Final Grade")
st.bar_chart(df[['absences', 'final_grade']])


