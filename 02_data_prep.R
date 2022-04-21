rm(list = ls())
gc()

library(pacman)
p_load(tidyverse, magrittr, lubridate)

raw_folder_name <- "raw_data"
files_in_raw_folder <- list.files(raw_folder_name)
coins_to_download <- crypto::crypto_list() %>% filter(rank<=51) %>% filter(symbol != "LEND") %>% select(symbol)  %>% as_vector()# Filter top 50 coins

df_all_coins <- data.frame()
for (f in files_in_raw_folder){
  if (all(substr(f, 1, nchar(f)-4) %in% coins_to_download)){
    df_coin <- read.csv(paste0(raw_folder_name,"/",f)) %>%
      arrange(time) %>%
      mutate(daily_return_pct = close/lag(close)-1, # Calculate daily return percentage
             intraday_return = close/open-1,
             daily_log_return = log(close) - log(lag(close))) # daily log return
    df_all_coins <- rbind(df_all_coins, df_coin)
  }
}
rm(df_coin)
summary(df_all_coins)
# get common min date for all coins
filter_date <- df_all_coins %>%
  filter((high+low+open+volumefrom+volumeto+close)!=0) %>%
  group_by(coin) %>%
  summarise(min = min(time),
            max = max(time)) %>% 
  summarise(filter_date = max(min)) %>% 
  as_vector() %>% ymd() + days(1) #Add one day to avoid getting Inf results for daily return calculations


df_all_coins %<>%
  filter(time >= filter_date)

write.csv(df_all_coins, "all_coins_data.csv",row.names = F)
