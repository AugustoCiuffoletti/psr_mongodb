import sys
import dns
import pymongo
from libri import libri

uri = 'mongodb+srv://<username>:<password>@examples.dfcdl.mongodb.net/<dbname>?retryWrites=true&w=majority' 
client = pymongo.MongoClient(uri)   # Connessione al server
db = client.get_default_database()  # Accesso al database
collezione = db['archivio']         # Selezione della collezione
collezione.insert_many(libri)       # Inserimento dall'array 'libri'
client.close()                      # Chiusura della connessione

