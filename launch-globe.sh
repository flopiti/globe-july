#!/bin/bash
# 🌍 Globe Launcher Script
# Simple script to start your spinning globe

echo "🌍 Welcome to the Spinning Globe Launcher!"
echo ""

# Check if ne_110m_land.json exists
if [ ! -f "ne_110m_land.json" ]; then
    echo "❌ Error: ne_110m_land.json not found in current directory"
    echo "Please make sure your land data file is in the same folder as this script."
    exit 1
fi

echo "📊 Found land data: ne_110m_land.json ($(du -h ne_110m_land.json | cut -f1))"
echo ""

# Check for Python
if command -v python3 &> /dev/null; then
    echo "🐍 Starting Python server..."
    python3 serve.py
elif command -v python &> /dev/null; then
    echo "🐍 Starting Python server..."
    python serve.py
else
    echo "❌ Python not found. Trying alternative methods..."
    
    # Check for Node.js http-server
    if command -v http-server &> /dev/null; then
        echo "📦 Starting Node.js http-server..."
        http-server -p 8000 --cors
    # Check for PHP
    elif command -v php &> /dev/null; then
        echo "🐘 Starting PHP server..."
        php -S localhost:8000
    else
        echo "❌ No suitable server found."
        echo ""
        echo "Please install one of the following:"
        echo "  • Python 3: https://python.org"
        echo "  • Node.js + http-server: npm install -g http-server"
        echo "  • PHP: https://php.net"
        echo ""
        echo "Then run this script again or:"
        echo "  python3 serve.py"
        exit 1
    fi
fi