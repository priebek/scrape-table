library("rvest")
url <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area"
population <- url %>%
  html() %>%
  html_nodes(xpath='/html/body/div[3]/div[3]/div[5]/div/table') %>%
  html_table()
population <- population[[1, 2]]

head(population)
