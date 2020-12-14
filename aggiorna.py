import sys
import dns
import pymongo

uri = 'mongodb+srv://<username>:<password>@examples.dfcdl.mongodb.net/<dbname>?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)    # Connessione al server
db = client.get_default_database()   # Accesso al DB
collezione = db['archivio']          # Selezione della collezione
collezione.update_one(
   {'titolo': 'The Life and Opinions of Tristam Shandy'}, # selezione del documento
   {'$set': {'autore': 'Laurence Sterne'}}                # modifica
)
client.close()                       # Chiusura della connessione

