import sys
import pymongo

uri = 'mongodb://user:password@ds111066.mlab.com:11066/example' 
client = pymongo.MongoClient(uri)
db = client.get_default_database()
collezione = db['archivio']
cursore = collezione.find({'prestito':False}).sort('autore',1)  # Creazione del cursore
for libro in cursore:                                           # Iterazione sul cursore
   print ('Autore: %s, Titolo: %s' %                            # Stampa del documento
          (libro['autore'], libro['titolo']))
client.close()

