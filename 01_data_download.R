rm(list = ls())
gc()
setwd("~/Documents/DMUBA/Tesis1/Crypto_NetworkAnalysis")

library(pacman)
p_load(cryptor, tidyverse)
coins <- crypto::crypto_list()

coins_to_download <- coins %>% filter(rank<=200) %>% select(symbol)

raw_folder_name <- "raw_data"
for (c in coins_to_download$symbol){
  if(!all(c %in% c("CCXX","ACA", "NXM","IZE","DRS","CRD", "CCCAGG"))){ # No data available for these coins
    print(paste0("Downloading historical data for: ", c))
    df_coin <- get_historical_price(fsym = c, tsym = "USD", all_data = T)
    df_coin$coin <- c
    write.csv(df_coin, paste0(raw_folder_name, "/", c, ".csv"), row.names = F)
    rm(df_coin)
  }
}