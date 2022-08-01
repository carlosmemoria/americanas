#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

st.set_page_config(layout="wide")

n = pd.value_counts(df['target']) [0]
e = pd.value_counts(df['target']) [1]

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
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=pd.value_counts(df['target']) [0], y=pd.value_counts(df['target']) [1])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig)

def graf():
	#Distribuição dos dados da classe Y (Não existe ocorrência = n, Existe ocorrência = e)

	n = pd.value_counts(df['target']) [0]
	e = pd.value_counts(df['target']) [1]

	condTrue = 'Não há ocorrência do evento que desejamos prever em '
	condFalse = 'Existe ocorrência do evento que desejamos prever '
	resposta = 'linhas'

	tam = len(df)

	pie = pd.DataFrame([['Há ocorrência',n],['Não há ocorrência',e]],columns=['Target' , 'Quant'])

	def pie_chart(data,col1,col2,title): 
		labels = {'Não':0,'Sim':1}
		sizes = data[col2]
		colors = ['#e5ffcc', '#f80032']

		plt.pie(sizes, labels=labels, colors=colors,
					autopct='%1.1f%%', shadow=True, startangle=140, labeldistance =1.2)
		plt.title( title )
		
		plt.axis('equal')
		plt.show()

	pie_chart(pie,'Target' , 'Quant','Distribuição Percentual quanto a existência ou não de ocorrência')

	print("\n")
	print("{}{}{}".format(condTrue,n," "+ resposta))
	print("{}{}{}".format(condFalse,e," "+ resposta))
	print("\n")

	plt.bar(pie.Target,pie.Quant, color = ['#e5ffcc', '#f80032'])
	plt.title("Distribuição quanto a existência ou não de ocorrência")
	plt.xlabel("Existe ocorrência?")
	plt.ylabel('Quantidade de Registros')
	plt.show()

def interactive_plot():
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

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
	graf()
elif options == 'Interactive Plots':
    interactive_plot()
