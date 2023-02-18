# -*- coding: utf-8 -*-
import unicodedata
import os
import json
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import googleapiclient.discovery 

def main():   

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    api_service_name        =   os.getenv("API_SERVICE_NAME")
    api_version             =   os.getenv("API_VERSION")
    location_coordinates    =   os.getenv("LOCATION_COORDINATES")
    developer_key           =   os.getenv("DEVELOPER_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = developer_key)

    request = youtube.search().list(
        part            =   os.getenv("PART"),
        location        =   os.getenv("LOCATION"),
        locationRadius  =   os.getenv("LOCATIONRADIUS"),
        maxResults      =   os.getenv("MAXRESULTS"),
        q               =   os.getenv("Q"),
        order           =   os.getenv("ORDER"),
        type            =   os.getenv("TYPE")
    )
    
    response = request.execute()
    return response

if __name__ == "__main__":
    main()