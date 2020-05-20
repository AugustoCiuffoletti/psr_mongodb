import sys
import pymongo

uri = 'mongodb://augusto:asterix11@ds111066.mlab.com:11066/example' 
# Connessione al server e 
client = pymongo.MongoClient(uri)
db = client.get_default_database()
db.drop_collection('archivio')
client.close()

