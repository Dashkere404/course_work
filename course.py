import kagglehub
import pandas as pd
# Загрузка датасета
path = kagglehub.dataset_download("kanametov/movies-recomendation-system")
movies_df=pd.read_csv(f"{path}/movies.csv")
links_df=pd.read_csv(f"{path}/links.csv")
ratings_df=pd.read_csv(f"{path}/ratings.csv")
tags_df=pd.read_csv(f"{path}/tags.csv")

#Удаление дубликатов, где это необходимо, а также строк, которые имеют хотя бы одно пустое значение
movies_df=movies_df.drop_duplicates(subset=['movieId']).dropna()
links_df=links_df.drop_duplicates(subset=['movieId']).dropna()
ratings_df=ratings_df.dropna()
tags_df=tags_df.dropna()

