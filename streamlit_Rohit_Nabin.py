import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Titanic Dataset")

df = pd.read_csv("\\titanic.csv")
st.dataframe(df)

st.subheader("Description of the dataset")
st.write(df.describe())

st.subheader("Survived Persons by Sex")
st.bar_chart(data=df, x="Sex", y="Survived")

st.subheader("Survived persons by Pclass")
st.bar_chart(data=df, x="Pclass", y="Survived")

st.subheader("Age Distribution")
age_data = df['Age']
fig, ax = plt.subplots()
ax.hist(age_data, bins=20)
ax.set_xlabel('Age')
ax.set_ylabel('Count')
st.pyplot(fig)

