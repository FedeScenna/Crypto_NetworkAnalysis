import matplotlib.pyplot as plt
import networkx as nx
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt


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

def plot_acfs(df,coins, num_rows, num_cols):
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15,18))
    # Flatten the axes array for easier iteration
    axes = axes.flatten()
    # Iterate over each coin
    for i, c in enumerate(coins):
        # Plot autocorrelation for each coin on a separate subplot
        ax = axes[i]
        plot_acf(df[df["coin"] == c]["close"], ax=ax,fft=True, auto_ylims=True)
        ax.set_title("Autocorrelation - " + c)
    # Remove empty subplots
    for i in range(len(coins), num_rows * num_cols):
        fig.delaxes(axes[i])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_pacfs(df,coins, num_rows, num_cols):
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15,18))
    # Flatten the axes array for easier iteration
    axes = axes.flatten()
    # Iterate over each coin
    for i, c in enumerate(coins):
        # Plot autocorrelation for each coin on a separate subplot
        ax = axes[i]
        plot_pacf(df[df["coin"] == c]["close"], ax=ax, auto_ylims=True)
        ax.set_title("Partial Autocorrelation - " + c)
    # Remove empty subplots
    for i in range(len(coins), num_rows * num_cols):
        fig.delaxes(axes[i])

    # Adjust layout
    plt.tight_layout()
    plt.show()