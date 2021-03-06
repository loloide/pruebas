from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080


with open("data.json", "r") as f:
    database = f.read()


data = ["martin,silva,36",
        "lorenzo,de la cruz,15",
        "koyomi,araragi,17",
        "suruga,kanbaru,16",
        "izuko,gaen,26",
        "ocelot,revolver,68,shalashaska",
        "sodachi,oikura,17",
        "shinobu,oshino,500+",
        "asriel,dremurr,20",
        "nadeko,sengoku,15",
        "kaiki,deishuu,40",
        "solid,snake,24",
        "hola,soy german,100",
        "july,3p,25",
        "a,g,4",
        "a,d,4"]



class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(database, "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")