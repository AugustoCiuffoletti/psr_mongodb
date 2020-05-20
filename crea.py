#!/usr/bin/python
import sys
import pymongo

libri = [
    {
        'scaffale': 'alto',
        'autore': 'L. Sterne',
        'titolo': 'The Life and Opinions of Tristam Shandy',
        'prestito': False
    },
    {
        'scaffale': 'medio',
        'autore': 'Edward Morgan Forster',
        'titolo': 'Passage to India',
        'prestito': True
    },
    {
        'scaffale': 'alto',
        'autore': 'Charles Dickens',
        'titolo': 'Great Expectations',
        'prestito': False
    },
    {
        'scaffale': 'basso',
        'autore': 'Charles Dickens',
        'titolo': 'Hard Times',
        'prestito': False
    }
]

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://augusto:asterix11@ds111066.mlab.com:11066/example' 
# Connessione al server e 
client = pymongo.MongoClient(uri)

db = client.get_default_database()
collezione = db['archivio']
collezione.insert_many(libri)

client.close()

