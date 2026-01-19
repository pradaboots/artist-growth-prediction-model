# PROJECT ROUGH PLAN – ARTIST GROWTH PREDICTION MODEL

## Objective

Create a data-driven model that assigns each artist a **growth score**, representing the likelihood of **rapid near-term growth** (i.e. “blowing up”) within the next **30 days**.

The output is a **ranked list of artists** with clear explanations for each score.

---

## What “Blowing Up” Means (Statistical Definition)

“Blowing up” is defined as **accelerated short-term growth**, not long-term fame.

This project focuses on **near-term growth** because:
- Artist growth today happens quickly.
- Platforms benefit from identifying momentum early.
- Short time windows are measurable using public data.

### Operational Definition (Proxy)

- An artist is considered to be “blowing up” if they exceed a defined **growth threshold** (e.g. follower or engagement growth) within a **30-day window**.

This definition serves as a **proxy label** for modeling purposes.

---

## Potential Data Sources (Exploratory)

These data sources are considered, but **not all are used**.

### Instagram
- Follower count
- Like count
- Like-to-follower ratio
- Reel views

### SoundCloud
- Plays over time
- Likes
- Reposts
- Number of tracks
- Upload timestamps

### Spotify
- Monthly listeners
- Number of tracks

### Apple Music
- Number of tracks

**Important:**
- Listing these sources demonstrates product awareness.
- Not using all of them demonstrates scope control and restraint.

---

## Selected Primary Data Source

### SoundCloud

**Reasoning:**
- Public and accessible data
- Strong signal for early-stage artists
- Clear engagement metrics
- Time-based activity signals (uploads, likes, reposts)

---

## Non-Goals

This project intentionally does **not** attempt to:
- Predict long-term fame
- Build a music recommender system
- Perform audio or signal processing
- Use deep learning for its own sake

**Why include this:**
- Prevents scope creep
- Signals engineering judgment
- Builds reviewer trust in modeling decisions

---

## Modeling Goal (Clarified)

The model will:
- Use engagement and activity signals
- Learn patterns associated with accelerating growth
- Output a **growth probability score** per artist
- Rank artists by growth likelihood

The model does **not** claim causation.  
It provides a **decision-support signal**.
