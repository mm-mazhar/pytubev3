#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Mazhar"
__credits__ = ["Mazhar"]
__Lisence__ = "BSD"
__maintainer__ = "Mazhar"
__email__ = "mazqoty.01@gmail.com"
__status__ = "Production"
__version__ = "1.0"

#Default Python Packages
import os, re, copy, warnings
warnings.filterwarnings("ignore")
from collections import Counter

#PIP installed Python Packages
from googleapiclient.discovery import build
#import googleapiclient.errors
from googleapiclient.errors import *
from iteration_utilities import unique_everseen

#Imports from other files
#from .my_file import OtherClass

class Pytube:
    
    def __init__(self, API_KEY: str, region_code = "US", lang = "en"):
        self.API_KEY = API_KEY
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.region_code = region_code
        self.lang = lang
        self.youtube = build(self.api_service_name, self.api_version, developerKey = self.API_KEY)
        
    ###################################################################################################
    ######################## Method to get video categories in specific region ########################
    ###################################################################################################
    def country_video_cat(self):
        """_summary_

        Returns:
            list: List of Dictionaries, with 'Video_Category_ID' and 'Title' of the Categories in the required country
        """
        
        country_video_Categories = []
        
        try:
            request = self.youtube.videoCategories().list(
                part = "snippet",
                hl = self.lang, # requires string: The hl parameter specifies the language that should be used for text values in the API response. The default value is en_US.
                regionCode = self.region_code
            )
            
            response = request.execute()
            
            for i in range(len(response["items"])):
                _videoCategories = dict(Video_Category_ID = response["items"][i]["id"],
                                    Title = response["items"][i]["snippet"]["title"]
                                    )
                country_video_Categories.append(_videoCategories)
        except Exception as e:
            print(f"Status Code: {e.status_code}")
            print(f"Error Reason: {e.reason}")
            print(f"Error Details: {e.error_details}")
            
        
        return country_video_Categories
    
    ####################################################################################################################################
    ######################## Method to Search Youtube Channels by Keyword and Location (Latitude and Longitude) ########################
    ####################################################################################################################################
    def chs_By_Keyword_Location(self, search_term: str, location_lat_long: str, location_radius = "10mi", required_results = 5, order_method = "relevance", published_after = "2010-01-01T00:00:00Z"):
        """_summary_

        Args:
            search_term (str): Specifies the query term to search for. 
                               e.g to search for videos matching either "boating" or "sailing" but not "fishing", 
                               set the q parameter value to boating|sailing -fishing.
            location_lat_long (str): The parameter value is a string that specifies latitude/longitude coordinates e.g. (37.42307,-122.08427)
            location_radius (str, optional): Used in conjunction with the location parameter, defines a circular geographic area. Defaults to "10mi".
            required_results (int, optional): Number of desired results. Defaults to 5.
            order_method (str, optional): Specifies the method that will be used to order resources. Acceptable values are rating, date, relevance, title, videoCount, viewCount. Defaults to "relevance".
            published_after (str, optional): Indicates that the response should only contain resources created at or after the specified time. Defaults to "2010-01-01T00:00:00Z".

        Returns:
            list: List of Dictionaries, with 'Channel_ID' and ''Channel_Title' of the Videos in the required location (latitude and longitude)
        """
        
        print(f"Searching For: '{search_term}' in '{self.lang}' language within the location radius of '{location_radius}' of Latitude and Longitude ({location_lat_long}) published after '{published_after}'")
        print(f"Number of Required Results {required_results}")
        
        channels_By_Kw_Loc = []
        
        try:
            request = self.youtube.search().list(
                part = "snippet",
                maxResults = 50,                    # Acceptable values are 0 to 50, inclusive.
                order = order_method,               # Acceptable values are rating, date, relevance, title, videoCount, viewCount. Default is 'relevance'.
                relevanceLanguage = self.lang,
                channelType = "any",                # Restrict a search to a particular type of channel. Acceptable values are 'any', 'show'.
                q = search_term,                    # Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms. 
                                                    # For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. 
                                                    # Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing. 
                type = "video",                     # Acceptable values are channel, playlist, video.
                location = location_lat_long,       # The parameter value is a string that specifies latitude/longitude coordinates e.g. (37.42307,-122.08427).
                locationRadius = location_radius,   # Valid measurement units are m, km, ft, and mi and Values must be less than 1000 kilometers.
                publishedAfter = published_after,
            )
            response = request.execute()
            
            for i in range(len(response["items"])):
                _channelsDetails = dict(Channel_ID = response["items"][i]["snippet"]["channelId"],
                                Channel_Title = response["items"][i]["snippet"]["channelTitle"])
                channels_By_Kw_Loc.append(_channelsDetails)
                
            # Using unique everseen() for Removing duplicate dictionaries in a list
            channels_By_Kw_Loc = list(unique_everseen(channels_By_Kw_Loc))
            print("Number of Results Achieved in First Attempt: ", len(channels_By_Kw_Loc))
                
            _next_page_token = response.get("nextPageToken")
            _generatedToken = 1
            _more_pages = True
            
            #print("Next Page Token: ", _next_page_token)
            _lenoflst = []
            
            while (_more_pages) and (len(channels_By_Kw_Loc) < required_results):
                if (_next_page_token is None):
                    _more_pages = False
                    print("Next Page Token: ", _next_page_token)
                    print(_more_pages)
                else:
                    print("Executing While Loop Else Block")
                    request = self.youtube.search().list(
                        part = "snippet",
                        maxResults = 50,                    # Acceptable values are 0 to 50, inclusive.
                        order = order_method,               # Acceptable values are rating, date, relevance, title, videoCount, viewCount. Default is 'relevance'.
                        relevanceLanguage = self.lang,      
                        channelType = "any",                # Restrict a search to a particular type of channel. Acceptable values are 'any', 'show'.
                        q = search_term,                    # Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms.
                                                            # For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. 
                                                            # Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing. 
                        type = "video",                     # Acceptable values are channel, playlist, video.
                        location = location_lat_long,       # The parameter value is a string that specifies latitude/longitude coordinates e.g. (37.42307,-122.08427).
                        locationRadius = location_radius,   # Valid measurement units are m, km, ft, and mi and Values must be less than 1000 kilometers.
                        publishedAfter = published_after,
                        
                    )
                    response = request.execute()

                    for i in range(len(response["items"])):
                        _channelsDetails = dict(Channel_ID = response["items"][i]["snippet"]["channelId"],
                                        Channel_Title = response["items"][i]["snippet"]["channelTitle"])
                        channels_By_Kw_Loc.append(_channelsDetails)

                    channels_By_Kw_Loc = list(unique_everseen(channels_By_Kw_Loc))
                    print("Len of channels_By_Kw_Loc: ", len(channels_By_Kw_Loc))
                    _lenoflst.append(len(channels_By_Kw_Loc))
                    print("Checking For Identical Results")
                    _counter = Counter(_lenoflst)
                    _result = max(_counter.values())
                    if (_result) >= 3:
                        print("Stoping Due to Insufficient Results or Duplicate Results")
                        break
                    _next_page_token = response.get("nextPageToken")
                    _generatedToken += 1
                    print(f"New Page Token Generated {_generatedToken} time(s)")
                    #print(f"New Page Token: {_next_page_token}")
                
                if len(channels_By_Kw_Loc) >= required_results:
                    print("Number of Required Results Achieved: ", len(channels_By_Kw_Loc))
                    break
        except Exception as e:
            print(f"Status Code: {e.status_code}")
            print(f"Error Reason: {e.reason}")
            print(f"Error Details: {e.error_details}")
                
                        
        return channels_By_Kw_Loc
    
    ##############################################################################################################
    ######################## Method to Search Youtube Channels by Keyword and Region Code ########################
    ##############################################################################################################
    def chs_By_Keyword_RegionCode(self, search_term: str, required_results = 5, order_method = "relevance", published_after = "2010-01-01T00:00:00Z"):
        """_summary_

        Args:
            search_term (str): Specifies the query term to search for. 
                               e.g to search for videos matching either "boating" or "sailing" but not "fishing", 
                               set the q parameter value to boating|sailing -fishing.
            required_results (int, optional): Number of desired results. Defaults to 5.
            order_method (str, optional): Specifies the method that will be used to order resources. Acceptable values are rating, date, relevance, title, videoCount, viewCount. Defaults to "relevance".
            published_after (str, optional): Indicates that the response should only contain resources created at or after the specified time. Defaults to "2010-01-01T00:00:00Z".

        Returns:
            list: List of Dictionaries, with 'Channel_ID' and ''Channel_Title' of the Videos in the specified region. 
        """
        
        print(f"Searching For: '{search_term}' in '{self.lang}' language within the region of ({self.region_code}) published after '{published_after}'")
        print(f"Number of Required Results {required_results}")
                
        channels_By_Kw_Region = []
        
        try:
            request = self.youtube.search().list(
                part = "snippet",
                maxResults = 50,                    # Acceptable values are 0 to 50, inclusive.
                order = order_method,               # Acceptable values are rating, date, relevance, title, videoCount, viewCount. Default is 'relevance'.
                regionCode = self.region_code,          
                relevanceLanguage = self.lang,
                channelType = "any",                # Restrict a search to a particular type of channel. Acceptable values are 'any', 'show'.
                type = "channel",
                q = search_term,                    # Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms. 
                                                    # For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. 
                                                    # Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing. 
                publishedAfter = published_after,
                
            )
            response = request.execute()
            
            for i in range(len(response["items"])):
                channelsDetails = dict(Channel_ID = response["items"][i]["snippet"]["channelId"],
                                Channel_Title = response["items"][i]["snippet"]["channelTitle"])
                channels_By_Kw_Region.append(channelsDetails)
                
            # Using unique everseen() for Removing duplicate dictionaries in a list
            channels_By_Kw_Region = list(unique_everseen(channels_By_Kw_Region))
            print("Number of Results Achieved in First Attempt: ", len(channels_By_Kw_Region))
                
            _next_page_token = response.get("nextPageToken")
            _generatedToken = 1
            _more_pages = True
            
            #print("Next Page Token: ", _next_page_token)
            _lenoflst = []
            
            while (_more_pages) and (len(channels_By_Kw_Region) < required_results):
                if (_next_page_token is None):
                    _more_pages = False
                    print("Next Page Token: ", _next_page_token)
                    print(_more_pages)
                else:
                    print("Executing While Loop Else Block")
                    request = self.youtube.search().list(
                        part = "snippet",
                        maxResults = 50,                    # Acceptable values are 0 to 50, inclusive.
                        order = order_method,               # Acceptable values are rating, date, relevance, title, videoCount, viewCount. Default is 'relevance'.    
                        regionCode = self.region_code,
                        relevanceLanguage = self.lang,
                        channelType = "any",
                        type = "channel",
                        q = search_term,                    # Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms. 
                                                            # For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. 
                                                            # Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing. 
                        publishedAfter = published_after,
                        
                    )
                    response = request.execute()

                    for i in range(len(response["items"])):
                        channelsDetails = dict(Channel_ID = response["items"][i]["snippet"]["channelId"],
                                        Channel_Title = response["items"][i]["snippet"]["channelTitle"])
                        channels_By_Kw_Region.append(channelsDetails)

                    channels_By_Kw_Region = list(unique_everseen(channels_By_Kw_Region))
                    print("Len of channels_By_Kw_Region: ", len(channels_By_Kw_Region))
                    _lenoflst.append(len(channels_By_Kw_Region))
                    print("Checking For Identical Results")
                    counter = Counter(_lenoflst)
                    result = max(counter.values())
                    if (result) >= 3:
                        print("Breaking While Loop Due to Insufficient Results")
                        break
                    _next_page_token = response.get("nextPageToken")
                    _generatedToken += 1
                    print(f"New Page Token Generated {_generatedToken} time(s)")
                    #print(f"New Page Token: {_next_page_token}")
                
                if len(channels_By_Kw_Region) >= required_results:
                    print("Number of Required Results Achieved: ", len(channels_By_Kw_Region))
                    break
        except Exception as e:
            print(f"Status Code: {e.status_code}")
            print(f"Error Reason: {e.reason}")
            print(f"Error Details: {e.error_details}")
                        
        
        return channels_By_Kw_Region
    
    ##############################################################################################################
    ################################## Method to get Channel's Stats #############################################
    ##############################################################################################################
    def channels_stats(self, channelIDs):
        """_summary_

        Args:
            channelIDs (list): list of youtube channels IDs

        Returns:
            list: list of dictionaries, containing stats of channels e.g subscriber count, views count, video count etc.
        """
        _channelStats = {}
        chsStats = []
        
        try:
            request = self.youtube.channels().list(part = "snippet, contentDetails, statistics, contentOwnerDetails, brandingSettings, localizations, status, topicDetails", 
                                            id = ",".join(channelIDs), maxResults = 50)
            response = request.execute()
            
            for i in range(len(response["items"])):
                
                try:
                    _channelStats["id"] = response['items'][i]['id']
                except Exception as e:
                    #print(e)
                    _channelStats["id"] = None

                try:
                    _channelStats["title"] = response['items'][i]['snippet']['title']
                except Exception as e:
                    #print(e)
                    _channelStats["title"] = None

                try:
                    _channelStats["description"] = response['items'][i]['snippet']['description']
                except Exception as e:
                    #print(e)
                    _channelStats["description"] = None

                try:
                    _channelStats["customUrl"] = response['items'][i]['snippet']['customUrl']
                except Exception as e:
                    #print(e)
                    _channelStats["customUrl"] = None

                try:
                    _channelStats["country"] = response['items'][i]['snippet']['country']
                except Exception as e:
                    #print(e)
                    _channelStats["country"] = None

                try:
                    _channelStats["contentDetails"] = response['items'][i]['contentDetails']
                except Exception as e:
                    #print(e)
                    _channelStats["contentDetails"] = None

                try:
                    _channelStats["keywords"] = response["items"][i]["brandingSettings"]["channel"]["keywords"]
                except Exception as e:
                    #print(e)
                    _channelStats["keywords"] = None

                try:
                    _channelStats["playlistId"] = response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
                except Exception as e:
                    #print(e)
                    _channelStats["playlistId"] = None

                try:
                    _channelStats["viewCount"] = response['items'][i]['statistics']['viewCount']
                except Exception as e:
                    #print(e)
                    _channelStats["viewCount"] = None

                try:
                    _channelStats["subscriberCount"] = response['items'][i]['statistics']['subscriberCount']
                except Exception as e:
                    #print(e)
                    _channelStats["subscriberCount"] = None

                try:
                    _channelStats["hiddenSubscriberCount"] = response['items'][i]['statistics']['hiddenSubscriberCount']
                except Exception as e:
                    #print(e)
                    _channelStats["hiddenSubscriberCount"] = None

                try:
                    _channelStats["videoCount"] = response['items'][i]['statistics']['videoCount']
                except Exception as e:
                    #print(e)
                    _channelStats["videoCount"] = None
                
                #print(_channelStats)
                _newDict = copy.deepcopy(_channelStats)
                chsStats.append(_newDict)
                #print(chsStats)
            
        except Exception as e:
            print(f"Status Code: {e.status_code}")
            print(f"Error Reason: {e.reason}")
            print(f"Error Details: {e.error_details}")
            
            
        return chsStats
    
    ##############################################################################################################
    ################################## Method to get Video IDs from Playlists ####################################
    ##############################################################################################################
    def video_ids(self, playlist_ids):
        """_summary_

        Args:
            playlist_ids (list): list of playlist ids

        Returns:
            list: list of dictionaries with channel_id, channel_title,  video_title, video_id
        """
        try:
            _responseLst = []
            _chVideoDetails = {}
            video_Ids = []
            for playlist_id in playlist_ids:
                request = self.youtube.playlistItems().list(
                    part = "contentDetails, id, snippet, status",
                    playlistId = playlist_id,
                    maxResults = 50,
                )
                response = request.execute()
                _responseLst.append(response)
            
            for i in range(len(_responseLst)):
                for j in range(len(_responseLst[i]['items'])):
                    try:
                        _chVideoDetails["channel_id"] = _responseLst[i]["items"][j]["snippet"]["channelId"]
                    except Exception as e:
                        _chVideoDetails["channel_id"] = None

                    try:
                        _chVideoDetails["channel_title"] = _responseLst[i]['items'][j]["snippet"]["channelTitle"]
                    except Exception as e:
                        _chVideoDetails["channel_title"] = None

                    try:
                        _chVideoDetails["video_title"] = _responseLst[i]['items'][j]["snippet"]["title"]
                    except Exception as e:
                        _chVideoDetails["video_title"] = None

                    try:
                        _chVideoDetails["video_id"] = _responseLst[i]['items'][j]["contentDetails"]["videoId"]
                    except Exception as e:
                        _chVideoDetails["video_id"] = None

                    _new_dict = copy.deepcopy(_chVideoDetails)
                    video_Ids.append(_new_dict)
            
        except Exception as e:
            print(f"Status Code: {e.status_code}")
            print(f"Error Reason: {e.reason}")
            print(f"Error Details: {e.error_details}")
        
        
        return video_Ids
    
    ##############################################################################################################
    ################################## Method to get Video Details ###############################################
    ##############################################################################################################
    def video_details(self, videoIds):
        """_summary_

        Args:
            videoIds (List): list of youtube's video IDs

        Returns:
            list: list of dictionaries with Title, Description, Published_Date, Likes, Favorite_Count, Comments_Count etc
        """
        try:
            video_stats = {}
            all_video_stats = []
            
            for i in range(0, len(videoIds), 50):
                request = self.youtube.videos().list(
                    part ="snippet, contentDetails, statistics",
                    id = ",".join(videoIds[i : i + 50])
                )
                response = request.execute()
            
                for video in response["items"]:
                    
                    try:
                        video_stats["Title"] = video["snippet"]["title"]
                    except Exception as e:
                        video_stats["Title"] = None
                        
                    try:
                        video_stats["Description"] = video["snippet"]["description"]
                    except Exception as e:
                        video_stats["Description"] = None
                    
                    try:
                        video_stats["Published_Date"] = video["snippet"]["publishedAt"]
                    except Exception as e:
                        video_stats["Published_Date"] = None
                        
                    try:
                        video_stats["Channel_Title"] = video["snippet"]["channelTitle"]
                    except Exception as e:
                        video_stats["Channel_Title"] = None
                    
                    try:
                        video_stats["Tags"] = video["snippet"]["tags"]
                    except Exception as e:
                        video_stats["Tags"] = None
                    
                    try:
                        video_stats["Duration"] = video["contentDetails"]["duration"]
                    except Exception as e:
                        video_stats["Duration"] = None
                        
                    try:
                        video_stats["Dimension"] = video["contentDetails"]["dimension"]
                    except Exception as e:
                        video_stats["Dimension"] = None
                    
                    try:
                        video_stats["Definition"] = video["contentDetails"]["definition"]
                    except Exception as e:
                        video_stats["Definition"] = None
                    
                    try:
                        video_stats["Caption"] = video["contentDetails"]["caption"]
                    except Exception as e:
                        video_stats["Caption"] = None
                    
                    try:
                        video_stats["Licensed_Content"] = video["contentDetails"]["licensedContent"]
                    except Exception as e:
                        video_stats["Licensed_Content"] = None
                        
                    try:
                        video_stats["Content_Rating"] = video["contentDetails"]["contentRating"]
                    except Exception as e:
                        video_stats["Content_Rating"] = None
                        
                    try:
                        video_stats["Projection"] = video["contentDetails"]["projection"]
                    except Exception as e:
                        video_stats["Projection"] = None
                        
                    try:
                        video_stats["Views"] = video["statistics"]["viewCount"]
                    except Exception as e:
                        video_stats["Views"] = None
                        
                    try:
                        video_stats["Likes"] = video["statistics"]["likeCount"]
                    except Exception as e:
                        video_stats["Likes"] = None
                        
                    try:
                        video_stats["Favorite_Count"] = video["statistics"]["favoriteCount"]
                    except Exception as e:
                        video_stats["Favorite_Count"] = None
                        
                    try:
                        video_stats["Comments_Count"] = video["statistics"]["commentCount"]
                    except Exception as e:
                        video_stats["Comments_Count"] = None
                    
                    newDict = copy.deepcopy(video_stats)
                    all_video_stats.append(newDict)
        except Exception as e:
            print(f"Status Code: {e.status_code}")
            print(f"Error Reason: {e.reason}")
            print(f"Error Details: {e.error_details}")
        
        
        return all_video_stats
       
    def __str__(self):
        return f"{Pytube}(api_service_name = {self.api_service_name}, api_version = {self.api_version}, region_code = {self.region_code}, lang = {self.lang})"
    
    def __repr__(self):
        return f'Pytube(api_service_name = {self.api_service_name}, api_version = {self.api_version}, region_code = {self.region_code}, lang = {self.lang})'