#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

condTrue = 'Não há ocorrência do evento que desejamos prever em '
condFalse = 'Existe ocorrência do evento que desejamos prever '
resposta = 'linhas'

st.set_page_config(layout="wide")
# Functions for each of the pages
def home(uploaded_file):

    if uploaded_file:
        st.header('Comece a explorar os dados usando o menu à esquerda')
    else:
        st.header('To begin please upload a file')

def data_describe():
    st.header('Estatísticas do Dataframe')
    st.write(df.describe())

    n = df['target'].value_counts() [0]
    e = df['target'].value_counts() [1]
	
    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))

def data_header():
    st.header('Cabeçalho do Dataframe')
    st.write(df.head())
	
    n = df['target'].value_counts() [0]
    e = df['target'].value_counts() [1]
	
    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))	

def bar_plot():

    st.header('Gráfico horizontall')
    fig = px.bar(x = [ df['target'].value_counts() [0], df['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	

    n = df['target'].value_counts() [0]
    e = df['target'].value_counts() [1]

    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))

#def displayplot(): 
	
def bar_plot():
    df_sample = df.sample(n=200)	
    st.header('Seleção aleatória de 200 entradas do dataset')
    fig = px.bar(x = [ df_sample['target'].value_counts() [0], df_sample['target'].value_counts() [1] ],
    y = ['Não atende','Atende'],
    title=" Tipos de dados ",
    labels={'x':'Quantidade','y':'Condição'},width=800, height=400)

    st.plotly_chart(fig)	

    n = df_sample['target'].value_counts() [0]
    e = df_sample['target'].value_counts() [1]

    st.write("{}{}{}".format(condTrue,n," "+ resposta))
    st.write("{}{}{}".format(condFalse,e," "+ resposta))	

# Add a title and intro text
st.title('Projeto de exploração de dados')
st.text('Este é um aplicativo web permite a exploração de dados em vários formatos de gráficos')

# Sidebar setup
st.sidebar.title('Área lateral')
upload_file = 'https://drive.google.com/u/0/uc?id=1HXq9mczY-5OpFaXK3kk8zAgFEgEgF3jt&export=download'
#Sidebar navigation
st.sidebar.title('Navegação')
options = st.sidebar.radio('Selecione o que deseja exibir:', ['Home', 'Resumo de Dados', 'Cabeçalho de dados', 'Gráfico de barras horizontal', 'Gráfico de dispersão', 'Interactive Plots'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_parquet(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Resumo de Dados':
    data_describe()
elif options == 'Cabeçalho de dados':
    data_header()
elif options == 'Gráfico de barras horizontal':	
	bar_plot()
elif options == 'Gráfico de dispersão':
    displayplot()
elif options == 'Interactive Plots':
    interactive_plot()
