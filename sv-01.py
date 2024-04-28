import http.server

class server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'sv-01')

servidor = http.server.HTTPServer(('localhost', 80), server)
servidor.serve_forever()
