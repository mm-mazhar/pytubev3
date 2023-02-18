from pytubev3 import Pytube
import os


if __name__ == '__main__':
    
    API_KEY = os.environ.get("YOUTUBE_DATA_API2")
    pT = Pytube(API_KEY, region_code = "US", lang = "en")
    channelIDs = ["UCdgU4pljNproO0RQVbT5QKg", "UC4Xt-DUAapAtkfaWWkv4OAw"]
    channels_stat = pT.channels_stats(channelIDs)
    print(channels_stat)