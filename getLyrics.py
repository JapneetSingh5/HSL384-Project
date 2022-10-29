import pickle
import pandas as pd
from tqdm import tqdm
import csv

token = 'BVUCPvV3k4iToDaobKg3khKmDJgFF1-92I5XSTJfvKo9tSCslVtXbV9dddCHyWRe';
import lyricsgenius
genius = lyricsgenius.Genius(token)

df = pd.read_csv('hot100_cleaned_1989.csv')
df_dict = df.to_dict('records')
f=open('lyrics_1989_2022.csv', 'a')
iter = 0
success = 0
failed = 0
csvw = csv.writer(f, delimiter=',')
csvw.writerow(['title', 'artist','lyrics'])
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
        # print(row['title'])
        song = artist.song(row['title'])
        if(song==None):
            csvw.writerow([row['title'], row['artist'],''])
            failed+=1
        elif(song.lyrics==None):
            csvw.writerow([row['title'], row['artist'],''])
            failed+=1
        else:
            csvw.writerow([row['title'], row['artist'], song.lyrics])
            success+=1
        # print(song.lyrics)
    f.flush()
print(f'Success count: {success}, Failure count: {failed}')

