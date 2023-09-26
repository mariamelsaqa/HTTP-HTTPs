from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler 
import ssl


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler )
httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="/Users/mariamelsaqa/Desktop/NetworksLab/Project/key.pem", 
        certfile='/Users/mariamelsaqa/Desktop/NetworksLab/Project/cert.pem', server_side=True)

httpd.serve_forever()
