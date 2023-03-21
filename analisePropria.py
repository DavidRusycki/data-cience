import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import json
import plotly.express as px

st.set_page_config(layout="wide")

@st.cache_data
def load_database():
    return pd.read_excel('BRCidadesRegiao.xlsx'), \
        json.load(open('brazil-states.geojson.txt'))

st.title('Minha análise própria - GCI')

cidades, fronteiras = load_database()

dados, estatistica, outlier, zvalues = st.tabs(['Dados', 'Estatística Descritiva', 'Outliers', 'Valores Padronizados'])

variaveis = [
 'codigo',
 'municipio',
 'estado',
 'area_territorial',
 'populacao_estimada',
 'densidade_demografica',
 'escolarizacao',
 'idhm',
 'pib_per_capita',
 'receitas_realizadas',
 'despesas_empenhadas',
 'saldo_receitas_despesas',
 'longitude',
 'latitude',
 'unidades',
 'unidades_urbanas',
 'unidades_rurais',
 'area_plantada',
 'producao_graos',
 'IDHM_Renda',
 'IDHM_Longevidade',
 'IDHM_Educacao',
 'tipo_rural_urbano'
 'GVA_agropecuaria',
 'GVA_industria',
 'GVA_Servicos',
 'GVA_publico GDP',
 'GDP_populacao',
 'GDP_per_capita',
 'estabelecimentos',
 'carros',
 'motos',
 'regiao_imediata'
]


with dados:
    if st.checkbox('Região'):
        regiao = st.selectbox('Selecione a Região:', cidades['regiao_imediata'].unique())
        st.dataframe(cidades[cidades['regiao_imediata'] == regiao])
    else:
        st.table(cidades)
    