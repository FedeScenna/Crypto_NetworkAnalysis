rm(list = ls())
gc()

library(pacman)
p_load(tidyverse, igraph, corrr)

df_all_coins <- read.csv("all_coins_data.csv")

min(df_all_coins$time)
max(df_all_coins$time)



get_matrix_from_coins <- function(data, metric){
  data %>%
    filter(!is.na(metric) & !is.infinite(metric) & !is.nan(metric)) %>%
    select(time, coin, metric) %>%
    pivot_wider(names_from = coin, values_from = metric) %>%
    select(-time) %>%
    corrr::correlate(diagonal = 0, use = "pairwise.complete.obs") %>%
    select(-term) %>% 
    as_matrix()
}

get_graph <- function(matrix){
  matrix %>%
    graph_from_adjacency_matrix(weighted = T, mode = "undirected", diag = F)
}

get_matrix_from_coins(df_all_coins, "intraday_return") %>% corrplot::corrplot(method = "color") 
  network_plot()
get_matrix_from_coins(df_all_coins, "daily_log_return") %>% network_plot()
get_matrix_from_coins(df_all_coins, "daily_return_pct") %>% network_plot()

get_matrix_from_coins(df_all_coins, "daily_return_pct") %>% 
  graph_from_adjacency_matrix(weighted = T, mode = "undirected", diag = F) %>% plot()


