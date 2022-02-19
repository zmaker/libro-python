from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

# Creiamo la classe che riceverà e risponderà alla richieste HTTP
class MyRequestHandler(BaseHTTPRequestHandler):
    # Implementiamo il metodo che risponde alle richieste GET
    def do_GET(self):
           	 
        now = datetime.now()
        print("now =", now)

        # dd/mm/YY H:M:S
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt)

        # Specifichiamo il codice di risposta
        self.send_response(200)
        # Specifichiamo uno o più header
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Specifichiamo il messaggio che costituirà il corpo della risposta
        message = "<html><head>"\
              	"<meta http-equiv='refresh' content='1'></head>"\
              	"<body>"\
              	"<h1>Ora esatta</h1>"\
              	"<p>" + dt + "</p></body></html>"
        self.wfile.write(bytes(message, "utf8"))
        return
    
def run():
    print('Avvio del server...')
    # Specifichiamo le impostazioni del server
    # Scegliamo la porta 8081 (per la porta 80 sono necessari i permessi di root)
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Server in esecuzione...')
    httpd.serve_forever()
    
    
if __name__ == "__main__":
    run()

