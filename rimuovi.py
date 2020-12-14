import sys
import pymongo

uri = 'mongodb://user:password@ds111066.mlab.com:11066/example'  
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db.drop_collection('archivio')      # Rimozione della collezione 'archivio'
client.close()

