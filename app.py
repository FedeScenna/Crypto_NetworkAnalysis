
import streamlit as st
import pandas as pd
from constants import stablecoins
import plotly.express as px
from utils import create_graph
import numpy as np
import networkx as nx

st.set_page_config(layout="wide")
st.title("Crypto Assets Graph Analysis")

# Return data----------------------------------------------------------------------------------------------------------
@st.cache_data
def read_df(file):
    return pd.read_csv(file)


df = read_df("st_return_data.csv")
df.replace({'stablecoin': {0: "Volátil", 1: "Paridad USD"}}, inplace = True)
st.dataframe(df)

st.title("Boxplot de retornos")
fig = px.box(data_frame=df, x = "coin",y="value", color = "stablecoin", labels={"coin":"Activo", "value":"Retorno Logarítmico", "stablecoin":"Tipo de Activo"})
st.plotly_chart(fig, use_container_width = True)

st.title("Resultados de clustering")
st.image("images/cluster_1.png")
st.image("images/cluster_2.png")
st.image("images/cluster_3.png")
st.image("images/cluster_4.png")
st.image("images/cluster_5.png")


st.title("Análisis de grafos")
corr_df = pd.read_csv("correlation_df.csv")
#Calculate corr range------------------------------------------------------------
corr_range = []
corr_range.append(corr_df["corr"].min())
while corr_range[-1]<corr_df["corr"].max():
    corr_range.append(corr_range[-1]+0.01)
corr_range.append(corr_df["corr"].max())
#--------------------------------------------------------------------------------

centrality_functions = {
    'Betweenness centrality': nx.betweenness_centrality,
    }

for f_name, f in centrality_functions.items():
    mean_values = []
    for c in corr_range:
        G = create_graph(corr_df[corr_df["corr"] > c], stablecoins)
        mean_values.append(np.mean(list(f(G).values())))
    fig = px.line(x = corr_range, y = mean_values, labels = {"x":"Correlation treshold", "y":f_name})
    fig.add_vline(x = 0.2)
    st.plotly_chart(fig, use_container_width = True)

fig = px.histogram(x = corr_df["corr"], labels = {"x":"Correlation distribution", "count":""})
fig.add_vline(x = 0.2)
st.plotly_chart(fig, use_container_width = True)

#df = pd.read_csv("graph_data.csv")
#nodes = list(set(df.coinfrom))#Get unique list of coins
#volatile_coins = [n for n in nodes if nodes not in stablecoins]
#
#
#nodes = set(df["coinfrom"].values.tolist())
#edges = []
#
#for index, row in df.iterrows():
#    edges.append( Edge(source=row["coinfrom"], 
#                   label="friend_of", 
#                   target=row["cointo"],)) 
#
#config = Config(width=750,
#                height=950,
#                directed=True, 
#                physics=True, 
#                hierarchical=False,
#                # **kwargs
#                )
#
#return_value = agraph(nodes=nodes, 
#                      edges=edges, 
#                      config=config)