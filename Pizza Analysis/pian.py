import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('pizza.csv')
print(df)
print(df.isna().sum())
print(df.duplicated().sum())