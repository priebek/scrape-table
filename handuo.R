library(tidyverse)
library(rvest)

df_get <- read_html("http://www.slyngel.dk/handuo/index.php") %>%
  html_table(fill = T) 

df_links <- read_html("http://www.slyngel.dk/handuo/index.php") %>%
  html_nodes("td:nth-child(2) a") %>% html_attr('href')

df <- df_get[[1]][-1, ] %>% bind_cols(links = df_links) %>% as_tibble() 

head(df)