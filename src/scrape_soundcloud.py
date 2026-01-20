import json
import re
import csv
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional
from pprint import pprint
from urllib.parse import urlparse


import requests
from bs4 import BeautifulSoup


@dataclass
class SoundCloudArtistSnapshot:
    """artist snapshot profile"""
    url: str
    scraped_at_utc: str
    artist_name: str
    followers_count: Optional[int]
    track_count: Optional[int]
    handle: str
    scrape_ok: bool
    http_status: int
    error: str = ""

    def to_row(self) -> dict:

        row = asdict(self)
        
        for k, v in row.items():
            if v is None:
                row[k] = ""
        return row


def get_page(url: str, timeout: int = 20) -> str:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0 Safari/537.36"
        )
    }
    r = requests.get(url, headers=headers, timeout=timeout)
    return r.text, r.status_code

def extract_meta_int(soup: BeautifulSoup, prop: str) -> Optional[int]:
    
    """
    Reads: <meta property="X" content="123">
    Returns int or None.
    """

    tag = soup.find("meta", attrs={"property": prop})

    if not tag:
        return None
    
    val = tag.get("content")

    if not val:
        return None
    
    val = val.strip()

    if not val.isdigit():
        return None
    return int(val)


def handle_from_url(url: str) -> str:
    """gets the artists handle directly from URL might be different to display name - more like username"""
    path = urlparse(url).path.strip("/")
    return path.split("/")[0] if path else ""

def scrape_profile(url: str) -> SoundCloudArtistSnapshot:
    snapshot_time = datetime.now(timezone.utc).isoformat()
    handle = handle_from_url(url)

    try:
        html, status = get_page(url)
        soup = BeautifulSoup(html, "html.parser")

        name_tag = soup.select_one(
            'noscript article[itemtype="http://schema.org/MusicGroup"] '
            'h1[itemprop="name"] a'
        )
        display_name = name_tag.get_text(strip=True) if name_tag else ""

        followers_count = extract_meta_int(soup, "soundcloud:follower_count")
        track_count = extract_meta_int(soup, "soundcloud:sound_count")

        scrape_ok = (status == 200) and (display_name != "" or followers_count is not None or track_count is not None)

        return SoundCloudArtistSnapshot(
            url=url,
            scraped_at_utc=snapshot_time,
            handle=handle,
            artist_name=display_name,
            followers_count=followers_count,
            track_count=track_count,
            http_status=status,
            scrape_ok=scrape_ok,
            error="",

        )

    except Exception as e:
        return SoundCloudArtistSnapshot(
            url=url,
            scraped_at_utc=snapshot_time,
            handle=handle,
            artist_name="",
            followers_count=None,
            track_count=None,
            http_status=0,
            scrape_ok=False,
            error=str(e),
        )
    

# to csv 

FIELDS = [
        "url",
        "scraped_at_utc",
        "handle",
        "artist_name",
        "followers_count",
        "track_count",
        "http_status",
        "scrape_ok",
        "error"
]

def append_snapshot_csv(csv_path: str, snapshot: SoundCloudArtistSnapshot):
    os.makedirs(os.path.dirname(csv_path) or ".",exist_ok = True)
    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if not file_exists:
            w.writeheader()
        w.writerow(snapshot.to_row())


if __name__ == "__main__":
    out_csv = "data/snapshots.csv"
    url = "https://soundcloud.com/user-695917221"

    snap = scrape_profile(url)
    print(snap)  # optional
    append_snapshot_csv(out_csv, snap)

    print(f"appended -> {out_csv}")


# pprint(scrape_profile('https://soundcloud.com/user-695917221'))
