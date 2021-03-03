from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
import urllib
import subprocess
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs

hostName = "localhost"
serverPort = 8080




class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        with open("data.json", "r") as f:
            database = f.read()
        self.wfile.write(bytes(database, "utf-8"))
    
    def parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(
                    self.rfile.read(length), 
                    keep_blank_values=1)
        else:
            postvars = {}
        return postvars

    def do_POST(self):
        self._set_headers()
        parsed_path = urllib.parse.urlparse(self.path)
        request_id = parsed_path.path

        postvars = self.parse_POST()

        with open("data.json", "r") as f:
            database = f.read()
        self.users = json.loads(database)
        self.wfile.write(bytes(database, "utf-8"))


        with open ("data.json", "w")as archivo_escribible:
            self.users["users"].append({
                "nombre":postvars[b"nombre"][0].decode("utf-8") ,
                "apellido":postvars[b"apellido"][0].decode("utf-8") ,
                "edad":postvars[b"edad"][0].decode("utf-8") 
            })
            archivo_escribible.write(json.dumps(self.users))
        
        verificar_edit = self.users["users"].append({
            "nombre":postvars[b"nombre"][0].decode("utf-8") ,
            "apellido":postvars[b"apellido"][0].decode("utf-8") ,
            "edad":postvars[b"edad"][0].decode("utf-8") 



if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")