# -*- coding: utf-8 -*-
import unicodedata
import os
import json
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import googleapiclient.discovery 

def main():   

    api_service_name    = "youtube"
    api_version         = "v3"

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    location_coordinates = os.getenv("LOCATION_COORDINATES")
    developer_key = os.getenv("DEVELOPER_KEY")

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = developer_key)

    request = youtube.search().list(
        part = "snippet",
        location=location_coordinates,
        locationRadius="200mi",
        maxResults=20,
        q="",
        order="date",
        type="video"
    )
    
    response = request.execute()
    return response

if __name__ == "__main__":
    main()