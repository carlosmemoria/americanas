#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

st.set_page_config(layout="wide")
# Functions for each of the pages
def home(uploaded_file):

    if uploaded_file:
        st.header('Comece a explorar os dados usando o menu à esquerda')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Estatísticas do Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Cabeçalho do Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data') 
    
    #fig = px.bar(y = [ df['target'].value_counts() [0], df['target'].value_counts() [1] ],
    fig = px.bar(train, x=[ df['target'].value_counts() [0], df['target'].value_counts() [1] ], y=['Não atende','Atende'], color="Sex", title=" Sobreviventes x Sexo ",
		 labels={'Sex': 'Sexo', 'Survived': 'Sobreviventes'},width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

def bar_plot():

    st.header('Gra´fico horizontall')
    fig = px.bar(x = [ df['target'].value_counts() [0], df['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    orientation='h', title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	
	
def interactive_plot():
    #col1, col2 = st.columns(2)
    
    #x_axis_val = col1.selectbox('Select the X-axis', options=df['target'].value_counts() [1])
    #y_axis_val = col2.selectbox('Select the Y-axis', options=df['target'].value_counts() [0])

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

# Add a title and intro text
st.title('Projeto de exploração de dados')
st.text('Este é um aplicativo web permite a exploração de dados em vários formatos de gráficos')

# Sidebar setup
st.sidebar.title('Área lateral')
upload_file = 'https://drive.google.com/u/0/uc?id=1HXq9mczY-5OpFaXK3kk8zAgFEgEgF3jt&export=download'
#Sidebar navigation
st.sidebar.title('Navegação')
options = st.sidebar.radio('Selecione o que deseja exibir:', ['Home', 'Resumo de Dados', 'Cabeçalho de dados', 'Gráfico de dispersão', 'Gráfico de barras horizontal', 'Interactive Plots'])

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
elif options == 'Gráfico de barras horizontal':	
	bar_plot()
elif options == 'Interactive Plots':
    interactive_plot()
