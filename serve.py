#!/usr/bin/env python3
"""
Simple HTTP server to serve the spinning globe files.
Handles CORS headers for local development.
"""

import http.server
import socketserver
import webbrowser
import os
from urllib.parse import urlparse

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

def serve_globe():
    PORT = 8000
    
    print("🌍 Starting Globe Server...")
    print(f"📡 Server running at: http://localhost:{PORT}")
    print("\n🎯 Globe available at:")
    print(f"   Globe: http://localhost:{PORT}/globe.html")
    print("\n📝 Files in directory:")
    
    # List relevant files
    files = [f for f in os.listdir('.') if f.endswith(('.html', '.json'))]
    for file in sorted(files):
        size = os.path.getsize(file) / 1024  # KB
        print(f"   📄 {file} ({size:.1f} KB)")
    
    print(f"\n🚀 Opening browser...")
    
    # Start server
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        # Open browser
        webbrowser.open(f'http://localhost:{PORT}/globe.html')
        
        print(f"\n✅ Server started! Press Ctrl+C to stop.")
        print("💡 Clean spinning globe with blue land on black background!")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped. Thanks for using Globe Server!")

if __name__ == "__main__":
    serve_globe()