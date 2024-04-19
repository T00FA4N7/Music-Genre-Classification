import pandas as pd
import glob

def combine_all(directory_path, store_path):
    # Get a list of all CSV files in a directory
    csv_files = glob.glob(directory_path+'/*.csv')

    # Create an empty dataframe to store the combined data
    combined_df = pd.DataFrame()

    # Loop through each CSV file and append its contents to the combined dataframe
    song_counts = {}
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        combined_df = pd.concat([combined_df, df])
        song_counts[df['Genre'][1]] = song_counts.get(df['Genre'][1], 0) + df.size/4
        
        print(df.size/4)
    
    combined_df.to_csv(store_path, index=False)
    print(song_counts)
combine_all('lyrics_en', 'combined_playlist_lyrics_en2.csv')