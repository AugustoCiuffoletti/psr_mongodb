#!/usr/bin/python
import sys
import pymongo

uri = 'mongodb://augusto:asterix11@ds111066.mlab.com:11066/example' 
# Connessione al server e 
client = pymongo.MongoClient(uri)
db = client.get_default_database()
collezione = db['archivio']
cursore = collezione.find({'prestito': False}).sort('autore', 1)
for libro in cursore:
   print ('Autore: %s, Titolo: %s' % (libro['autore'], libro['titolo']))
client.close()

