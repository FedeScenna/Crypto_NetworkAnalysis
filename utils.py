import matplotlib.pyplot as plt
import networkx as nx



def chart_ts(df, row_nr, coins_list):
    ax = plt.gca()
    plt.plot(df['time'],df[coins_list[row_nr]])
    ax.set_xticks(ax.get_xticks()[::45])
    plt.xlabel("Time")
    plt.ylabel("Daily log Return")
    plt.title(coins_list[row_nr])


def create_graph(corr_df, stablecoins, volatile_coins): 
    G = nx.Graph()
    coins = list(corr_df["coinfrom"]) + list(corr_df["cointo"])
    coins = set(coins)
    for c in coins:
        if c in stablecoins: 
            G.add_node(c, type = "stablecoin")
        else: 
            G.add_node(c, type = "volatile")
    relations = list(zip(corr_df["coinfrom"], corr_df["cointo"], corr_df["corr"]))
    [G.add_edge(l[0], l[1], weight = l[2]) for l in relations]
    return G