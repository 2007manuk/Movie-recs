import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer

def clean(df,column,header):
    cnt=0
    for i in df.loc[0:,column]:
        l=""
        for j in ast.literal_eval(i):
            l+=(j[header])+" "
        df.loc[cnt,column]=str(l)
        cnt+=1
    
def make_soup(df,pos,column):
    global soup
    if pd.isnull(df.loc[pos,column]) or df.loc[pos,column]=="[]":
        soup+=""
    else:
        soup=soup+str(df.loc[pos,column])+" "

movies_df=pd.read_csv("Movie-recs/data/tmdb_5000_movies.csv")
credits_df=pd.read_csv("Movie-recs/data/tmdb_5000_credits.csv")
#a=input("Enter a movie name: ")
merged_df=movies_df.merge(credits_df,left_on='id',right_on='movie_id')
merged_df=merged_df.drop(columns=["movie_id","budget","homepage","original_language","title_y","release_date","popularity","production_companies","production_countries","revenue","runtime","spoken_languages","status","tagline"])

clean(merged_df,"genres","name")
clean(merged_df,"keywords","name")
clean(merged_df,"cast","name")

cnt=0
for i in merged_df.loc[0:,"crew"]:
    l=""
    for j in ast.literal_eval(i):
        if j["job"] == "Director":
            l+=(j["name"])
    merged_df.loc[cnt,"crew"]=str(l)
    cnt+=1

global soup
soup=""

for i in range(len(merged_df)):
    soup=""
    make_soup(merged_df,i,"genres")
    make_soup(merged_df,i,"keywords")
    make_soup(merged_df,i,"cast")
    make_soup(merged_df,i,"crew")
    make_soup(merged_df,i,"overview")
    merged_df.loc[i,"soup"]=soup
    
u=list(merged_df["soup"])
v=TfidfVectorizer()
x=v.fit_transform(u)
print(type(x))