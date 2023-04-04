import os
import pandas as pd

import sqlalchemy
from sqlalchemy.engine import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text, Table, MetaData, Column, Integer, String, DateTime, Date


class Pipeline:
    """
    This class defines a data processing pipeline. The transform and load part are both made here.
    """
    @staticmethod
    def dataResponseValidation(resp):
        """
        Validate the response data.

        :param resp: The response the API gave us in a JSON format.
        """
        if resp is None:
            return "The entire JSON file is empty."

    @staticmethod
    def dataTransformation(df: pd.DataFrame):
        """
        Transform the data in the DataFrame.

        :param df: A pandas dataframe with the organized data of the response.
        """
        df['publishTime']   =   pd.to_datetime(df['publishTime'], format='%Y-%m-%d')
        df['publishTime']   =   df['publishTime'].dt.tz_convert(None)

        df['title']         =   df['title'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df['title']         =   df["title"].str.replace(r'[^A-Za-z ]', '')
        df['title']         =   df['title'].str.strip()

        df['description']   =   df['description'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df['description']   =   df["description"].str.replace(r'[^A-Za-z ]', '')
        df['description']   =   df['description'].str.strip()

    @staticmethod
    def dataInsert(df: pd.DataFrame):
        """
        Insert the transformed data into a relational database.
        
        :param df: A pandas dataframe with the organized data of the response.
        """
        connection_string   =   os.getenv("CONNECTION_STRING")
        connection_url      =   URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        engine              =   create_engine(connection_url)

        with engine.connect() as conn:

            insp = sqlalchemy.inspect(engine)
            print("Checking something")
            print(insp.has_table("YoutubeCRLastVideos")) 

            df.to_sql(con=engine, name='YoutubeCRLastVideos', if_exists='replace', index=True, dtype={
                'etag': String,
                'publishTime': String,
                'title': String,
                'description': String,
                'registeredInTable': String})
            

            
                        



            
                
            
                