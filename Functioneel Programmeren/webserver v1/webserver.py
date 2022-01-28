# source from https://pythonbasics.org/webserver/

from http.server import BaseHTTPRequestHandler, HTTPServer
from webserver_SQL_functies import get_sqldata

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/films': tabel = get_sqldata(self.path)
        elif self.path == '/gemeenten': tabel = get_sqldata(self.path)
        else: tabel = "geen data opgevraagd"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html_file = open('webserver_pagina.html', 'r')
        content = html_file.read()
        content = content.replace('@@placeholder voor data@@', tabel)
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

