import kagglehub
import pandas as pd
# Download latest version
path = kagglehub.dataset_download("kanametov/movies-recomendation-system")
movies_df=pd.read_csv(f"{path}/movies.csv")
links_df=pd.read_csv(f"{path}/links.csv")
ratings_df=pd.read_csv(f"{path}/ratings.csv")
tags_dfh=pd.read_csv(f"{path}/tags.csv")
print ("path: ", path)
print(movies_df["title"])
print(links_df.head())


