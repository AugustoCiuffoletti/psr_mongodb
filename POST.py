import httplib, urllib, json
api_key="la vostra apiKey"
# Il documento da inserire come oggetto Python (insieme di coppie chiave-valore)
document = {
  "text":"Hallo!",
  "author":"augusto"
}
document_json=json.JSONEncoder().encode(document)               # Lo codifico in JSON
conn = httplib.HTTPSConnection("api.mlab.com")                  # Apro la connessione
conn.request(
  "POST",                                                       # metodo HTTP
  "/api/1/databases/example/collections/dati?apiKey="+api_key,  # URL
  document_json,                                                # HTTP body
  {"Content-type": "application/json"}                          # HTTP header
)
response = conn.getresponse()
print response.status, response.reason
print response.read()
conn.close()
