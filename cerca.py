import sys
import dns
import pymongo

uri = 'mongodb+srv://<username>:<password>@examples.dfcdl.mongodb.net/<dbname>?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client.get_default_database()
collezione = db['archivio']
cursore = collezione.find({'prestito':False}).sort('autore',1)  # Creazione del cursore
for libro in cursore:                                           # Iterazione sul cursore
   print ('Autore: %s, Titolo: %s' %                            # Stampa del documento
          (libro['autore'], libro['titolo']))
client.close()

