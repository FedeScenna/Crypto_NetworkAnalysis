
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd
from constants import stablecoins


st.set_page_config(layout="wide")
st.title("Crypto Assets Graph Analysis")

df = pd.read_csv("graph_data.csv")
nodes = list(set(df.coinfrom))#Get unique list of coins
volatile_coins = [n for n in nodes if nodes not in stablecoins]


nodes = set(df["coinfrom"].values.tolist())
edges = []

for index, row in df.iterrows():
    edges.append( Edge(source=row["coinfrom"], 
                   label="friend_of", 
                   target=row["cointo"],)) 

config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)