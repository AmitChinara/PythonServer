from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import Data as data


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = urlparse(self.path).query
        query_components = parse_qs(query)

        if 'data' in query_components:
            data_key = query_components['data'][0]
            if data_key == '1':
                response_data = data.data1
            elif data_key == '2':
                response_data = data.data2
            else:
                response_data = "Invalid data key"
        else:
            response_data = "No data key provided"

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response_data.encode())


class Main:

    def __init__(self, port):
        self.port = port

    def main(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print(f"Server running on port {self.port}...")
        httpd.serve_forever()


if __name__ == '__main__':
    port = 8000  # You can choose any port that's not in use
    main = Main(port)
    main.main()
