#Loading Libraries
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

st.title("Data Visualization with Matplotlib and Seaborn")
#We will use the iris dataset
df = pd.read_csv("iris.csv")

#Display the dataset
st.text("1. Displaying the Dataframe")
st.dataframe(df)

#Simple Distplot
st.text("2. Bar plot using Matplotlib")
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

#Plot using Seaborn
st.text("3. Using Seaborn")
fig = plt.figure()
sns.distplot(df['sepal_length'])
st.pyplot(fig)

#Multiple graphs in 1 column
col1, col2 = st.columns(2)
with col1:    
    col1.header = "KDE=False"
    col1.write("KDE=False")
    fig1 = plt.figure()
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)
    
with col2:
    col2.header = "Hist=False"
    col2.write("Hist=False")
    fig2 = plt.figure()
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig2)
    
    
#Changing Styles
st.text("3. Chainging styles")
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig)  
with col2:
    fig = plt.figure()
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig)
   

#Scatterplot
st.text("4. Scatter Plot")
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)


#Countplot
st.text("5. Countplot")
fig = plt.figure(figsize=(15,8))
sns.countplot(data=df,x = 'species')
st.pyplot(fig)


#BoxPlot
st.text("6. Boxplot")
fig = plt.figure(figsize=(15,8))
sns.boxplot(data=df, x = "species",y="petal_length",saturation=1)
st.pyplot(fig)

#ViolinPLot
st.text("7. ViolinPlot")
fig = plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="species",y="petal_length",saturation=1)
st.pyplot(fig)


