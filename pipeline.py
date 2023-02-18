import pandas as pd, pyodbc, os, time
from unidecode import unidecode
from datetime import datetime
from sqlalchemy.engine import create_engine, URL
from sqlalchemy import text


class Pipeline:

    def dataResponseValidation(self, resp):
        try:
            if(resp != None):
                pass
            elif(resp == None):
                return ("The entire JSON file is empty.")
        except ValueError:
                return ("Something went wrong.")


    def dataTransformation(self, df):
        df['publishTime']   =   pd.to_datetime(df['publishTime'], format='%Y-%m-%d')
        df['publishTime']   =   df['publishTime'].dt.tz_convert(None)

        df['title']         =   df['title'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df['title']         =   df["title"].str.replace(r'[^A-Za-z ]', '')
        df['title']         =   df['title'].str.strip()

        df['description']   =   df['description'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df['description']   =   df["description"].str.replace(r'[^A-Za-z ]', '')
        df['description']   =   df['description'].str.strip()

    def dataInsert(self, df):
        ##Note to add a possible catch if the credentials in the connection_string are incorrect.
        connection_string   = os.getenv("CONNECTION_STRING")
        connection_url      = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        engine              = create_engine(connection_url)

        with engine.connect() as conn:
            ##conn.execute(text(query))
            df.to_sql('YoutubeCRLastVideos', index=True, index_label=id, con=engine, if_exists='append', method='multi')