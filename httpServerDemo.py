import http.server
import socketserver
port=9000
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",port),Handler) as httpd:
    print("Serving at port ",port)
    print("Pradeep")
    httpd.serve_forever()