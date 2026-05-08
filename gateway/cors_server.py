from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

os.chdir("/app/data")

server = HTTPServer(("0.0.0.0", 8000), CORSRequestHandler)

print("[*] CORS-enabled dashboard server running on port 8000")

server.serve_forever()