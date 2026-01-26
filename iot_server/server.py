from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print("Received data:", body.decode(), flush=True)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

print("IoT Cloud Server running on port 8080...")
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()