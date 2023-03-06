# -*- coding: utf-8 -*-
import unicodedata
import os
import json
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import googleapiclient.discovery 

def main():   

    # Load environment variables/path automatically.
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    # Constants
    API_SERVICE_NAME        =   os.getenv("API_SERVICE_NAME")
    API_VERSION             =   os.getenv("API_VERSION")
    DEVELOPER_KEY           =   os.getenv("DEVELOPER_KEY")
    PART                    =   os.getenv("PART")
    LOCATION                =   os.getenv("LOCATION")
    LOCATIONRADIUS          =   os.getenv("LOCATIONRADIUS")
    MAXRESULTS              =   os.getenv("MAXRESULTS")
    Q                       =   os.getenv("Q")
    ORDER                   =   os.getenv("ORDER")
    TYPE                    =   os.getenv("TYPE")

    # Start building the YouTube API client.
    youtube = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, developerKey = DEVELOPER_KEY)

    # Search for videos to be received in the request.
    request = youtube.search().list(
        part            =   PART,
        location        =   LOCATION,
        locationRadius  =   LOCATIONRADIUS,
        maxResults      =   MAXRESULTS,
        q               =   Q,
        order           =   ORDER,
        type            =   TYPE
    )
    
    # Execute the request and then return a response.
    try:
        response = request.execute()
        return response
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()