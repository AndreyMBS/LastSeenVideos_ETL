import os
import json
from datetime import datetime

import pandas as pd

from pipeline import Pipeline
from dotenv import load_dotenv, find_dotenv
import youtube_search_list


if __name__ == '__main__':

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    ACCEPT      = os.getenv("ACCEPT")
    CONTENTTYPE = os.getenv("CONTENTTYPE")

    headers = {
        "Accept"        : ACCEPT,
        "Content-Type"  : CONTENTTYPE,
    }

    data_processed = Pipeline()

    data = json.dumps(youtube_search_list.main())
    resp = json.loads(data)

    data_processed.dataResponseValidation(resp)

    etag            = []
    publishTime     = []
    title           = []
    description     = []

    dataArray = resp['items']
    for i in range(len(dataArray)): 
        etag.append(resp['items'][i]['etag'])
        publishTime.append(resp['items'][i]['snippet']['publishedAt'])
        title.append(resp['items'][i]['snippet']['title'])
        description.append(resp['items'][i]['snippet']['description'])

    dict_videos = {
        "etag"              :   etag,
        "publishTime"       :   publishTime,
        "title"             :   title,
        "description"       :   description,
        "registeredInTable" :   datetime.now()
    }

    video_df = pd.DataFrame(dict_videos, columns = ["etag", "publishTime", "title", "description", "registeredInTable"])
    data_processed.dataTransformation(video_df)
    data_processed.dataInsert(video_df)