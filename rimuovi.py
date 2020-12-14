import sys
import dns
import pymongo

uri = 'mongodb+srv://<username>:<password>@examples.dfcdl.mongodb.net/<dbname>?retryWrites=true&w=majority'  
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db.drop_collection('archivio')      # Rimozione della collezione 'archivio'
client.close()

