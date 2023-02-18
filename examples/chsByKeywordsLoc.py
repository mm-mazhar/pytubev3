from pytubev3 import Pytube
import os


if __name__ == '__main__':
    
    API_KEY = os.environ.get("YOUTUBE_DATA_API2")
    pT = Pytube(API_KEY, region_code = "US", lang = "en")
    channels = pT.chs_By_Keyword_Location(search_term = "Python", location_lat_long = "37.42307,-122.08427", \
                                         location_radius = "10mi", required_results = 5, \
                                         order_method = "relevance", published_after = "2010-01-01T00:00:00Z")
    print(channels)