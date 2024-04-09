import http.server
import socketserver
import json
import sys

count = 0

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        global count
        if count < 10:
            count += 1
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Webhook request received. Total requests: {}'.format(count), 'utf-8'))
        else:
            self.send_response(503)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Maximum number of requests reached. Shutting down.', 'utf-8'))
            sys.exit()

if __name__ == '__main__':
    server = socketserver.TCPServer(('', 8000), WebhookHandler)
    print('Server started. Listening on port 8000...')
    server.serve_forever()