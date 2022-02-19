from http.server import BaseHTTPRequestHandler, HTTPServer
#from urlparse import urlparse, parse_qs
from urllib.parse import urlparse, parse_qs

# Creiamo la classe che riceverà e risponderà alla richieste HTTP
class MyRequestHandler(BaseHTTPRequestHandler):
    # Implementiamo il metodo che risponde alle richieste GET
    def do_GET(self):
        print("path:",self.path)
        data = urlparse(self.path)   	 
        print("dati:", data)
        param = parse_qs(data.query)
        print("parametri:", param)

        message = "<html><body><h1>Pagina dinamica con parametri</h1>"
        
        if '/led' in self.path:
            print("1")
            msg = "Stato del LED: "
            state = 'off'
            color = 'white'
                 
            if 'state' in param:
                state = param['state'][0]

            if 'color' in param:
                color = param['color'][0]
             
            if (state == 'on'):
                msg += "ON"
            else:
                msg += "OFF"
            
            
            message += "<p>" + msg  + "</p>"
            message += f"<div style='width:50; height:50; background:{color};'></div>"
            message += "</body></html>"
        else:
            print("2")
            message = "<h1>???</h1>"
            message += "</body></html>"
    
        # Specifichiamo il codice di risposta
        self.send_response(200)
        # Specifichiamo uno o più header
        self.send_header('Content-type','text/html')
        self.end_headers()
        
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

