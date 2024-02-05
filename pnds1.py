# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1. Title and subheader
st.title('Data Analysis')
st.subheader('Data Analysis using Python/Stream.lit')

#2. Upload Dataset
upload=st.file_uploader("Upload your Dataset(in CSV format)")
if upload is not None :
    data=pd.read_csv(upload)

#3 show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button('Head'):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
    

#4 Check Dataset of each column
if upload is not None :
    if st.checkbox("Data type of each column"):
        st.text('Datatype')
        st.write(data.dtypes)
        
#5 Find the shape of our Dataset (Number of Rows and Number of columns)
if upload is not None :
     data_shape = st.radio("Do you want to show?", ("Rows", "Columns"))
     if data_shape == 'Rows':
         st.text("No. of Rows")       
         st.write(data.shape[0])
     if data_shape == 'Columns':
         st.text("No. of Columns")
         st.write(data.shape[1])
            
#6 Find Null values in the Dataset
if upload is not None:
    st.text("Check Null values in Dataset")
    test=data.isnull().values.any()
    if test==True:
        st.checkbox("Check null values in Dataset")
        sns.heatmap(data.isnull())
    #    plt.subplot(data.shape[0],data.shape[1])        
    else:
        st.text("Success, No Null values found in this Dataset")
        
#7 Find duplicate values in Dataset
if upload is not None:
    dup=data.duplicated().any()        
    if dup==True:
        st.warning("Dataset has duplicate value")
        dup=st.selectbox("Do you want to remove duplicate value?" \
                         ("Select One","Yes","NO"))
        if dup=='Yes':
            data=dup.duplicates()
            st.text("Duplicate values are removed")
        if dup=='No' :
            st.text("No problem")

#8 Get overall statistics

if upload is not None :
    if st.checkbox("Summary of the Dataset"):
        st.text(data.describe(include="all"))
        
# 9 About Section
    if st.checkbox("About App"):
        st.text("Built with Streamlit")
        st.text("Thanks Streamlit")
        
# 10 By
    if st.checkbox("By"):
       st.success("By Nilabja Basak")
       




            
            
            
            
            
            
            
            
            
            
            
        
        
    
    
    

        
       
    
        
