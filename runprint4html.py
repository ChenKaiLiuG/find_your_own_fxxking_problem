from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get_file_content':
            filename = '找找自己問題.txt'
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'File not found.')
        else:
            super().do_GET()

if __name__ == '__main__':
    port = 8000
    httpd = HTTPServer(('localhost', port), MyHandler)
    print(f"Serving on port {port}")
    httpd.serve_forever()
