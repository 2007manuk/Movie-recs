import pandas as pd
import ast

def clean(df,column,header):
    cnt=0
    for i in df.loc[0:,column]:
        l=[]
        for j in ast.literal_eval(i):
            l.append(j[header])
        df.loc[cnt,column]=str(l)
        cnt+=1


movies_df=pd.read_csv("Movie-recs/data/tmdb_5000_movies.csv")
credits_df=pd.read_csv("Movie-recs/data/tmdb_5000_credits.csv")
#a=input("Enter a movie name: ")
merged_df=movies_df.merge(credits_df,left_on='id',right_on='movie_id')
merged_df=merged_df.drop(columns=["movie_id","budget","homepage","original_language","release_date","popularity","production_companies","production_countries","revenue","runtime","spoken_languages","status","tagline"])

print(merged_df.loc[7])


clean(merged_df,"genres","name")
clean(merged_df,"keywords","name")
clean(merged_df,"cast","name")
clean(merged_df,"crew","name")
"""cnt=0
for i in merged_df.loc[0:,"genres"]:
    l=[]
    for j in ast.literal_eval(i):
        l.append(j["name"])
    merged_df.loc[cnt,"genres"]=str(l)
    cnt+=1"""

print(merged_df.loc[7])

