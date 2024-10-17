library(tidyverse)
source('https://raw.githubusercontent.com/declanrjb/declanrjb-r/refs/heads/main/functions.R')

df <- read_csv('data/investigations_all.csv')

df <- df %>% select(!INST_TYPE)

df$INVEST_START_DATES <- df$INVEST_START_DATES %>% mdy()
df$CAL_YEAR <- year(df$INVEST_START_DATES)

df['STATUTE'] <- df$DISCRIMINATION_TYPE %>% str_split_i('-',1) %>% str_squish()
df['VIOLATION'] <- df$DISCRIMINATION_TYPE %>% str_split_i('-',2) %>% str_squish()
