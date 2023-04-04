import os
import json
from datetime import datetime
import datetime

import pandas as pd

from pipeline import Pipeline
from dotenv import load_dotenv, find_dotenv
from youtube_api import YoutubeAPI

def main():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    # Load headers from environment variables
    ACCEPT      = os.getenv("ACCEPT")
    CONTENTTYPE = os.getenv("CONTENTTYPE")

    headers = {
        "Accept"        : ACCEPT,
        "Content-Type"  : CONTENTTYPE,
    }

    # Retrieve data from Youtube API transforming the first response into JSON.
    data = json.dumps(YoutubeAPI.connection_to_api())
    resp = json.loads(data)

    # Validate the response.
    Pipeline.dataResponseValidation(resp)

    etag            = []
    publishTime     = []
    title           = []
    description     = []

     # Extract the values from the response using a for cycle.
    dataArray = resp['items']
    for i in range(len(dataArray)): 
        etag.append(resp['items'][i]['etag'])
        publishTime.append(resp['items'][i]['snippet']['publishedAt'])
        title.append(resp['items'][i]['snippet']['title'])
        description.append(resp['items'][i]['snippet']['description'])

    # Create a dictionary to save the data collected before.
    dict_videos = {
        "etag"              :   etag,
        "publishTime"       :   publishTime,
        "title"             :   title,
        "description"       :   description,
        "registeredInTable" :   datetime.datetime.now()
    }

    # Create pandas dataframe from video data
    video_df = pd.DataFrame(dict_videos, columns = ["etag", "publishTime", "title", "description", "registeredInTable"])

    # Perform data transformation
    Pipeline.dataTransformation(video_df)

     # Insert data into database
    Pipeline.dataInsert(video_df)

if __name__ == "__main__":
    main()