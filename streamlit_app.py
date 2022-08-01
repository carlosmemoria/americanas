#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df['target'].value_counts() [0])

def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(0,1)
    ax.scatter(x=df['target'].value_counts() [0], y=df['target'].value_counts() [1])
    ax.set_xlabel('target')
    ax.set_ylabel('target')
    
    st.pyplot(fig)

def bar_plot():

	x = ["sim", "não"]
	y = [0, 1]
	bar(x, y,leg =false) 


def interactive_plot():
    #col1, col2 = st.columns(2)
    
    #x_axis_val = col1.selectbox('Select the X-axis', options=df['target'].value_counts() [1])
    #y_axis_val = col2.selectbox('Select the Y-axis', options=df['target'].value_counts() [0])

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = 'https://drive.google.com/u/0/uc?id=1HXq9mczY-5OpFaXK3kk8zAgFEgEgF3jt&export=download'
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Resumo de Dados', 'Cabeçalho de dados', 'Gráfico de dispersão', 'Gráfico', 'Interactive Plots'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_parquet(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Resumo de Dados':
    data_summary()
elif options == 'Cabeçalho de dados':
    data_header()
elif options == 'Gráfico de dispersão':
    displayplot()
elif options == 'Gráfico':	
	bar_plot()
elif options == 'Interactive Plots':
    interactive_plot()
