from math import nan
import pickle
from numpy import NaN
import pandas as pd
from tqdm import tqdm
import csv
import math

token = 'BVUCPvV3k4iToDaobKg3khKmDJgFF1-92I5XSTJfvKo9tSCslVtXbV9dddCHyWRe';
import lyricsgenius
genius = lyricsgenius.Genius(token)

df = pd.read_csv('song_lyrics_missing_scraped.csv')
df_dict = df.to_dict('records')
iter = 0
success = 0
failed = 0
print(df_dict[0])
row_count = 0
for row in tqdm(df_dict):
    row_count += 1
    if(row_count<12600):
        continue
    if(not isinstance(row['Lyrics'], str) and math.isnan(row['Lyrics'])):
        print(f'Success count: {success}, Failure count: {failed}')
        print(row['title'])
        try:
            # iter+=1
            # if(iter==10):
            #     break
            # print(row['artist'])
            artist = genius.search_artist(row['artist'], allow_name_change=True, max_songs=0)
            if(artist==None):
                failed+=1
                print("Not found")
                # csvw.writerow([row['title'], row['artist'], ''])
            else:
                # print(row['title'])
                song = artist.song(row['title'])
                if(song==None):
                    print("Not found")
                    # csvw.writerow([row['title'], row['artist'],''])
                    failed+=1
                elif(song.lyrics==None):
                    print("Not found")
                    # csvw.writerow([row['title'], row['artist'],''])
                    failed+=1
                else:
                    row['Lyrics'] = song.lyrics.replace(',',' ').replace('"',' ').replace('\n', ' ')
                    # csvw.writerow([row['title'], row['artist'], song.lyrics])
                    success+=1
                # print(song.lyrics)
        except:
            print("Exception \n")
    if(success%300==0 and success>0):
        print("writing to csv..")
        dfw = pd.DataFrame.from_dict(df_dict)
        dfw.to_csv('song_lyrics_missing_scraped_iter2.csv', index = False, header=True)
df = pd.DataFrame.from_dict(df_dict)
df.to_csv('song_lyrics_missing_scraped_iter2.csv', index = False, header=True)
with open('df_dict.pkl', 'wb') as file:
    pickle.dump(df_dict, file)


