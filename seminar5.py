import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("do_GET")

        self.send_response(200, 'ok')
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = "You asked for {}".format(self.path[1:])
        self.wfile.write(bytes('Hello there handsome!', 'utf8'))        

httpd = HTTPServer(('localhost', 8000), handler)
httpd.serve_forever()
