from langdetect import detect
from langdetect import DetectorFactory
import pandas as pd
import re

# genres = [
#     'blues', 
#     'classical', 
#     'Country',
#     'disco', 
#     'hiphop', 
#     'jazz',
#     'metal', 
#     'pop', 
#     'reggae',
#     'rock'
# ]

def filter_en(file_path, new_file_path):
    columns = ['Artist', 'Track', 'Lyrics', 'Genre']
    df1 = pd.read_csv(file_path)
    df2 = pd.DataFrame(columns=columns)
    for ind in df1.index:
        try:
            lang = detect(df1['Lyrics'][ind])
        except:
            continue
        if lang == 'en':
            df2 = df2._append(df1.iloc[ind], ignore_index=True)
        print(ind)
    df2.to_csv(new_file_path, index=False)

def clean_lyrics(file_path, new_file_path):
    df1 = pd.read_csv(file_path)
    def clean_helper(lyrics):
        if (lyrics == -1 or lyrics == '-1'): return -1
        if lyrics.find('Lyrics') != -1:
            lyrics = lyrics[lyrics.find("Lyrics")+len('Lyrics'):]
        lyrics = (re.sub("\[.*?\]", '', lyrics))
        lyrics = lyrics.replace('Embed', '')
        lyrics = lyrics.replace('You might also like', '')
        regex = re.compile('[^a-zA-Z0-9 \n]')
        lyrics = re.sub(regex, '', lyrics)
        return lyrics.strip()
    df1['Lyrics'] = df1['Lyrics'].apply(clean_helper)
    df1.to_csv(new_file_path, index=False)
    
clean_lyrics('test_set.csv', 'test_set_cleaned.csv')