import os

file_url = os.getenv("FILE_URL")

def read():

    """
    Reads a certain file to ensure it's data type.
    """

    file = open(file_url, "r", encoding="utf-8")
    type(file)

if __name__ == '__main__':
    read()
