import pickle
import pandas as pd
from tqdm import tqdm
import csv

token = 'BVUCPvV3k4iToDaobKg3khKmDJgFF1-92I5XSTJfvKo9tSCslVtXbV9dddCHyWRe';
import lyricsgenius
genius = lyricsgenius.Genius(token)

df = pd.read_csv('hot100_cleaned.csv')
df_dict = df.to_dict('records')
f=open('lyrics.csv', 'a')
f.write('title,artist,lyrics\n')
iter = 0
success = 0
failed = 0
csvw = csv.writer(f, delimiter=',')
for row in tqdm(df_dict):
    iter+=1
    if(iter==10):
        break
    # print(row['artist'])
    artist = genius.search_artist(row['artist'], allow_name_change=True, max_songs=0)
    if(artist==None):
        failed+=1
        # print("Not found")
        csvw.writerow([row['title'], row['artist'], ''])
    else:
        success+=1
        # print(row['title'])
        song = artist.song(row['title'])
        csvw.writerow([row['title'], row['artist'], song.lyrics])
        # print(song.lyrics)
    f.flush()
print(success, failed)


print(df.head())

# artist = genius.search_artist("The Platters", max_songs=1, sort="title")
# # print(artist.songs)



# res = genius.search_song
