
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd
from constants import stablecoins
import plotly.express as px


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