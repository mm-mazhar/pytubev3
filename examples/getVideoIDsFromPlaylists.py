from pytubev3 import Pytube
import os


if __name__ == '__main__':
    
    API_KEY = os.environ.get("YOUTUBE_DATA_API2")
    pT = Pytube(API_KEY, region_code = "US", lang = "en")
    playlist_ids = ["UUdgU4pljNproO0RQVbT5QKg"]
    videoIDs = pT.video_ids(playlist_ids)
    print(videoIDs)