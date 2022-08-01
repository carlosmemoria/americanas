# importando as bibliotecas
import streamlit as st
import matplotlib as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
from PIL import Image

df = pd.read_parquet('https://drive.google.com/u/0/uc?id=1HXq9mczY-5OpFaXK3kk8zAgFEgEgF3jt&export=download')
st.dataframe(df)

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
#Tipos de variaveis
fig = px.bar(x = [6,5],
            y = ['Categóricas','Numéricas'],
            orientation='h', title=" Tipos de dados ",
             labels={'x':'Target','y':'Quant'},width=800, height=400)
st.plotly_chart(fig)
