import pandas as pd

# Load the first CSV file with lyrics
lyrics_df = pd.read_csv('lyrics.csv')

# Load the second CSV file with genre
genre_df = pd.read_csv('audio_features.csv')

# Merge the two dataframes based on the 'track' and 'artist' columns
merged_df = pd.merge(lyrics_df, genre_df, on=['track', 'artist'], how='inner')

# Select only the desired columns
result_df = merged_df[['track', 'artist', 'lyrics', 'genre']]

# Write the result to a new CSV file
result_df.to_csv('combined.csv', index=False)