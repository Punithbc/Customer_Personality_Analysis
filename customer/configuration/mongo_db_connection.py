import pymongo
from customer.constant.database import DATABASE_NAME, COLLECTION_NAME
from customer.constant.env_variable import MONGO_DB_URL
import certifi
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url ="mongodb+srv://Punith:aVQXgiu3s6YFtvEE@cluster0.uelehlq.mongodb.net/test"
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e                     
