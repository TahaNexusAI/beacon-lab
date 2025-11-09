from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/ping"):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"pong")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print("Serving on http://127.0.0.1:8000 ...")
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
