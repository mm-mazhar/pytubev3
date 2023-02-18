# Pytubev3


<div align="center">
  
  <a href="">![text](https://img.shields.io/badge/Python-3.7+-3776AB?style=plastic&logo=Python)</a>
  <a href="">![text](https://img.shields.io/badge/PyPI-3775A9?style=plastic&logo=PyPI)</a>

</div>


### DESCRIPTION

A wrapper around youtube API v3: _pytubev3_ is a genuine, lightweight, dependency-free Python library to simplify Youtube Data API tasks.
-   [https://developers.google.com/youtube/v3/docs/](https://developers.google.com/youtube/v3/docs/)

### Actively soliciting contributors!

Have ideas for how pytube can be improved? Feel free to open an issue or a pull request!
Also looking forward for contributors to have fully functional wrapper.

## GOAL

Created this package to simplify some typical tasks related to the Youtube API. See the examples/usage.

## Quickstart

This guide covers the most basic usage of the library.

### Installation

Pytubev3 requires an installation of Python 3.7 or greater, as well as pip. (Pip is typically bundled with Python  [installations](https://python.org/downloads).)

To install from PyPI with pip:

`python -m pip install pytubev3`

## USAGE

Create an object
```
from pytubev3 import Pytube
import os

#set API Key as environment variable
#API_KEY = os.environ.get("YOUTUBE_DATA_API2")
#or
API_KEY = "Enter Your API Key"
pT = Pytube(API_KEY, region_code = "US", lang = "en")
```

## Examples

The  class provides a set of methods for interacting with the YouTube API. The methods include:

##### Get Video Categories of a Region
```
vid_cat = pT.country_video_cat()
print(vid_cat)
```
##### Search Youtube Channels by Keyword and Location (Latitude and Longitude)
```
channels = pT.chs_By_Keyword_Location(search_term = "Python", \
			location_lat_long = "37.42307,-122.08427", \
			location_radius = "10mi", required_results = 5, \
			order_method = "relevance", \
			published_after = "2010-01-01T00:00:00Z")

print(channels)
```

##### Search Youtube Channels by Keyword and Region Code
```
pT = Pytube(API_KEY, region_code = "US", lang = "en")
channels = pT.chs_By_Keyword_RegionCode(search_term = "Python", \
			required_results = 5, order_method = "relevance", \
			published_after = "2010-01-01T00:00:00Z")

print(channels)
```

##### Get Channel's Stats By Using Channel IDs
```
pT = Pytube(API_KEY, region_code = "US", lang = "en")
channelIDs = ["UCdgU4pljNproO0RQVbT5QKg", "UC4Xt-DUAapAtkfaWWkv4OAw"]
channels_stat = pT.channels_stats(channelIDs)
print(channels_stat)
```

##### Get Video IDs from Playlists by Using Playlist IDs
```
pT = Pytube(API_KEY, region_code = "US", lang = "en")
playlist_ids = ["UUdgU4pljNproO0RQVbT5QKg"]
videoIDs = pT.video_ids(playlist_ids)
print(videoIDs)
```

###### Get Video Details by using Video IDs
```
pT = Pytube(API_KEY, region_code = "US", lang = "en")
videoIds = ["sUg-XFx4xf0", "QCyz936VoYM"]
videoDetails = pT.video_details(videoIds)
print(videoDetails)
```
## Development/Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: ` git commit -am 'Add Some Feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.
6. Email me at `mazqoty.01@gmail.com` because I do not check those messages often.

## History
* 1.0.0 - Initial Commit without tests 
