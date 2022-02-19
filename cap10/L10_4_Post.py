from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib

class MyRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(b'<html>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<form method="POST">')
        self.wfile.write(b'<span>Nome:</span>\
                        <input name="nome"> \
                        <button>Invia</button>')
        self.wfile.write(b'</form>')    
        self.wfile.write(b'</body></html>')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        (input,value) = self.rfile.read(content_length).decode('utf-8').split('=')
        value = urllib.parse.unquote_plus(value)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        #self.wfile.write(b'<head><style>p, button {font-size: 1em}</style></head>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<p>Ciao, ' + bytes(value,'utf-8') + b'</p>')
        self.wfile.write(b'<a href="/">BACK</a>')
        self.wfile.write(b'</body>')    
 
def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()

