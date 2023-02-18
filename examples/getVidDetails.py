from pytubev3 import Pytube
import os


if __name__ == '__main__':
    
    API_KEY = os.environ.get("YOUTUBE_DATA_API2")
    pT = Pytube(API_KEY, region_code = "US", lang = "en")
    videoIds = ["sUg-XFx4xf0", "QCyz936VoYM"]
    videoDetails = pT.video_details(videoIds)
    print(videoDetails)