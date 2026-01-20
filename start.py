import numpy as np
import pandas as pd

# Initial artist seed structure
artists = [
    {
        "artist_name": "",
        "soundcloud_url": "",
        "follower_count_estimate": ""
    }
]

df = pd.DataFrame(artists)

# Save to CSV
df.to_csv("data/raw/artist_seed_list.csv", index=False)

print("artist_seed_list.csv created in data/raw/")