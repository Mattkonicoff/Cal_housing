import streamlit as st
import pandas as pd
import matplotlib as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Matthew Konicoff')
df_housing = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price', 0, 500001, 200000) #min, max, default

location_filter = st.sidebar.multiselect(
    'Choose the location',
    df_housing.ocean_proximity.unique(),
    df_housing.ocean_proximity.unique())

income_filter = st.sidebar.radio(
    'Choose the location'
    ('Low', 'Medium', 'High'))

df_housing = df_housing[df_housing.median_house_value <= price_filter]
df_housing = df_housing[df_housing.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
    df_housing = df_housing[(df_housing.median_income <= 2.5)]
elif income_filter == 'Medium':
    df_housing = df_housing[(df_housing.median_income < 2.5)] & (df_housing.median_income < 4.5)]
else:
    df_housing = df_housing[(df_housing.median_income >= 4.5)] 
    
st.subheader('Seaborn more filters in the sidebar')
st.map(df_housing)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
df_housing.median_house_value.hist(ax=ax, bins=30)
st.pyplot(fig)