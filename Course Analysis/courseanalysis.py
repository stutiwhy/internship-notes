import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('Database.csv')
# print(df)
# print(df.isna().sum())
# print(df.duplicated().sum())

st.title("Exploratory Data Analysis: Hospital")

st.subheader("Original Dataset :")
st.write(df)
st.write(df.shape)

st.subheader("Number of NULL values : ")
st.write(df.isnull().sum())

st.subheader("Number of duplicate values : ")
st.write(df.duplicated().sum())

ch = st.selectbox('Choose column', df.columns, index = 9)

# st.write(df['ch'].value_counts())
# st.write(df['ch'].value_counts().index) # prints left side(key)
# st.write(df['ch'].value_counts().values) # prints right side(value)

st.subheader("Bar Chart for selected column :")
st.bar_chart(df[ch].head(30), color='#90EE90')

st.subheader("Line Chart for selected column :")
st.line_chart(df[ch].head(30), color='#90EE90')

st.subheader("Scatter Chart for selected column :")
st.scatter_chart(df[ch].head(30), color='#90EE90')

st.subheader("Pie Chart for selected column :")
plt.figure(figsize = (10,10))
plt.pie(df[ch].head(30).value_counts().values, labels = df[ch].head(30).value_counts().index, colors=('#90EE90', 'grey'), autopct = '%1.2F%%')
st.pyplot(plt)

st.subheader("Barh for selected column : ")
plt.figure(figsize = (10,10))
plt.barh(df[ch].head(30).value_counts().values, width = 6, color = '#90EE90')
st.pyplot(plt)