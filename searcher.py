import json
import youtube_search_list
import pandas as pd

if __name__ == '__main__':

    headers = {
        "Accept": "application/json",
        "Content-Type" : "application/json",
    }

    data = json.dumps(youtube_search_list.main())
    resp = json.loads(data)

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
        "etag": etag,
        "publishTime": publishTime,
        "title": title,
        "description": description
    }

    video_df = pd.DataFrame(dict_videos, columns = ["etag", "publishTime", "title", "description"])
    print(video_df)