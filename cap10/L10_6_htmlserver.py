from http.server import BaseHTTPRequestHandler, HTTPServer
# Creiamo la classe che riceverà e risponderà alla richieste HTTP

class MyRequestHandler(BaseHTTPRequestHandler):
    # Implementiamo il metodo che risponde alle richieste GET
    def do_GET(self):
        print("path:",self.path)
        # Specifichiamo il codice di risposta
        self.send_response(200)
        # Specifichiamo uno o più header
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        basedir = "www"

        if (self.path == "/"):
            self.path += "index.html"
 
      
        with open(basedir+self.path) as reader:
            lines = reader.readlines()
            for l in lines:
                self.wfile.write(bytes(l, "utf8"))    
 
        return
    
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




