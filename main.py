from http.server import BaseHTTPRequestHandler, HTTPServer
from os import environ
import json
from actions import ban_ip, unban_ip


class http_handler(BaseHTTPRequestHandler):
    def _verify_auth(self) -> bool:
        auth_token = self.headers.get('Authorization')

        if not auth_token:
            return False

        if len(auth_token) < 6:
            return False

        if auth_token != environ.get('AUTH_TOKEN'):
            return False

        return True

    def do_GET(self):
        # Verify Authorization
        if not self._verify_auth():
            self.send_response(401, "Unauthorized")
            self.end_headers()
            return

        self.send_response(501, "Not Implemented")
        self.end_headers()

    def do_POST(self):
        # Verify Authorization

        if not self._verify_auth():
            self.send_response(401, "Unauthorized")
            self.end_headers()
            return

        # Verify Content Type
        content_type = self.headers.get('content-type')

        if content_type != 'application/json':
            self.send_response(400, "Expected application/json")
            self.end_headers()
            return

        # Read JSON from request
        message_len = int(self.headers.get('content-length'))

        try:
            data = json.loads(self.rfile.read(message_len))
        except:
            self.send_response(400, "Invalid JSON")
            self.end_headers()
            return

        success = True

        if 'ban' in data:
            if not ban_ip(data['ban']):
                success = False

        if 'unban' in data:
            if not unban_ip(data['unban']):
                success = False

        if success:
            self.send_response(200, "Request Completed")
        else:
            self.send_response(
                400, "An error ocurred during execution of 1 or more requests")

        self.end_headers()


def main():
    hostname = environ.get('HOST') or '127.0.0.1'
    port = environ.get('PORT') or 8085

    web_server = HTTPServer((hostname, port), http_handler)

    print(f"HTTP Server listening on {hostname}:{port}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        print("Server shutting down")
        web_server.socket.close()


if __name__ == '__main__':
    main()
