import json
from http.server import BaseHTTPRequestHandler, HTTPServer
# Creiamo la classe che riceverà e risponderà alla richieste HTTP

class MyRequestHandler(BaseHTTPRequestHandler):
    # Implementiamo il metodo che risponde alle richieste GET
    def do_GET(self):
        
        data = None
        if '/hello' in self.path:
            data = json.dumps({'hello': 'world', 'received': 'ok'})
        else:
            data = json.dumps({'error': 'not found'})
            
        # Specifichiamo il codice di risposta
        self.send_response(200)
        # Specifichiamo uno o più header
        self.send_header('Content-type','application/json')
        self.end_headers()
        # Specifichiamo il messaggio che costituirà il corpo della risposta
        
        
        self.wfile.write(bytes(data, "utf8"))
    
def run():
    print('Avvio del server...')
    # Specifichiamo le impostazioni del server
    # Scegliamo la porta 8081 (per la porta 80 
    #sono necessari i permessi di root)
    server_address = ('127.0.0.1', 8081)

    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Server in esecuzione...')
    httpd.serve_forever()
    
if __name__ == "__main__":
    run()



