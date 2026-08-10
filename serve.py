import http.server

print("http://localhost:8000")
http.server.HTTPServer(("", 8000), http.server.SimpleHTTPRequestHandler).serve_forever()
