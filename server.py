from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
import urllib
import subprocess

hostName = "localhost"
serverPort = 8080


with open("data.json", "r") as f:
    database = f.read()


class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(database, "utf-8"))
    
    
    def do_POST(self):
        self._set_headers()
        parsed_path = urllib.parse.urlparse(self.path)
        request_id = parsed_path.path
        response = subprocess.check_output(["data.json", request_id])
        self.wfile.write(json.dumps(response))

        
        



if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")