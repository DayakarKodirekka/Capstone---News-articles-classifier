import pymongo
import pandas as pd
from pymongo import MongoClient

# Load csv dataset
data = pd.read_csv('BBCdata1.csv')
# Connect to MongoDB
client =  MongoClient("mongodb+srv://Dayakar:3292%40wtt@clustertest-icsum.mongodb.net/test?retryWrites=true&w=majority")
db = client['newsDb']
collection = db['news']
data.reset_index(inplace=True)
data_dict = data.to_dict("records")
# Insert collection
collection.insert_many(data_dict)