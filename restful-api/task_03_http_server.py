#!/usr/bin/python3
"""Module compiled with Python3"""
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')


httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
print("serving at port", 8000)
httpd.serve_forever()

