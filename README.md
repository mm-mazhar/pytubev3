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
# API_KEY = os.environ.get("YOUTUBE_DATA_API2")
#or
API_KEY = "Enter Your API Key"
pT = Pytube(API_KEY, region_code = "US", lang = "en")

```

## Features

The  class provides a set of methods for interacting with the YouTube API. The methods include:

##### Get Video Categories of a Region

```
from pytubev3 import Pytube

vid_cat = pT.country_video_cat()
print(vid_cat)
```
