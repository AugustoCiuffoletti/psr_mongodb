import httplib, json
api_key="la vostra apiKey"
conn = httplib.HTTPSConnection("api.mlab.com")  # Apro la connessione
# Invio la request
conn.request(
  "GET",                                        # metodo HTTP
  "/api/1/databases?apiKey="+api_key            # HTTP header
)
response = conn.getresponse()
print response.status, response.reason
print response.read()
conn.close()
