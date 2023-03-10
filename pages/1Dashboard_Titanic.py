import streamlit as st
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Titanic_img.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "test _titanic.csv")

st.title("Dashboard - Titanic Data")

img = image.imread(IMAGE_PATH)
st.image(img)

s = st.subheader("Titanic_Data Set")


df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Pclass = st.selectbox("Select the Class:", df['Pclass'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Pclass'] == Pclass], x="Fare")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Pclass'] == Pclass], y="Fare")
col2.plotly_chart(fig_2, use_container_width=True)


Sex = st.selectbox("Select the Gender:", df['Sex'].unique())


col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df["Sex"] == Sex], x="Age")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df[df["Sex"] == Sex], y="Age")
col2.plotly_chart(fig_2, use_container_width=True)



