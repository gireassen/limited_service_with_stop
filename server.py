import http.server
import socketserver
from typing import NoReturn

MAX_REQUESTS = 10
PORT = 8008

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    count = 0

    def do_POST(self) -> None:
        self.__class__.count += 1
        
        if self.__class__.count <= MAX_REQUESTS:
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            response = f'Webhook request received. Total requests: {self.__class__.count}'
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_error_response_and_shutdown()

    def send_error_response_and_shutdown(self) -> NoReturn:
        self.send_response(503)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Maximum number of requests reached. Shutting down.')
        raise SystemExit(0)

def run_server() -> None:
    with socketserver.TCPServer(('', PORT), WebhookHandler) as server:
        print(f'Server started. Listening on port {PORT}...')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by user")

if __name__ == '__main__':
    run_server()