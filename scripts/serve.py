#!/usr/bin/env python3
"""Preview server: bind 0.0.0.0, allow iframe/preview hosts."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)


class H(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".js": "application/javascript",
        ".mjs": "application/javascript",
        ".json": "application/json",
        ".webp": "image/webp",
        ".mp4": "video/mp4",
        ".mp3": "audio/mpeg",
        ".woff2": "font/woff2",
    }

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        # allow embedding in Arena preview
        self.send_header("Content-Security-Policy", "frame-ancestors *")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    httpd = ThreadingHTTPServer(("0.0.0.0", 8080), H)
    print("serving", ROOT, "on 0.0.0.0:8080", flush=True)
    httpd.serve_forever()
