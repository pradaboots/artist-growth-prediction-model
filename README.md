# artist-growth-prediction-model
This model works by taking inputs of artists and giving them a score which is the probability of rapid near-term growth

PROJECT ROUGH PLAN – ARTIST GROWTH PREDICTION MODEL
Objective
Create a data driven model that assigns each artist a growth score, representing the likelihood of rapid near-term growth (i.e. “blowing up”) within the next 30 days.
The output is a ranked list of artists with explanations for the score. What “blowing up” means (statistical definition)
“Blowing up” is defined as accelerated short-term growth, not long-term fame.
This project focuses on near-term growth, because:
•	Artist growth today happens quickly.
•	Platforms benefit from identifying momentum early.
•	Short windows are measurable with public data.
Operational definition :
•	An artist is considered to be “blowing up” if they exceed a defined growth threshold (e.g. follower or engagement growth) within a 30-day window.
 
Potential data sources (exploratory)
These are considered but not all used.
•	Instagram
o	Follower count
o	Like count
o	Like-to-follower ratio
o	Reel views
•	SoundCloud
o	Plays over time
o	Likes
o	Reposts
o	Number of tracks
o	Upload timestamps
•	Spotify
o	Monthly listeners
o	Number of tracks
•	Apple Music
o	Number of tracks
Important:
Listing these shows product awareness.
Not using all of them shows restraint.
 
Selected primary data source
SoundCloud 
Reasoning:
•	Public, accessible data
•	Strong signal for early-stage artists
•	Clear engagement metrics
•	Time-based activity (uploads, likes, reposts)
 
Non-goals
This project intentionally does not attempt to:
•	Predict long-term fame
•	Build a music recommender system
•	Perform audio or signal processing
•	Use deep learning for its own sake
Why include this:
•	Prevents scope creep
•	Signals engineering judgment
•	Makes reviewers trust your choices
 


Modeling goal (clarified)
The model will:
•	Use engagement and activity signals
•	Learn patterns associated with accelerating growth
•	Output a growth probability score per artist
•	Rank artists by growth likelihood
The model does not claim causation.
It provides a decision-support signal.

