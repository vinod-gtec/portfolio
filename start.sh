#!/bin/bash

echo "🎯 Vinod Kumar Portfolio - Flask Backend"
echo "=================================================="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.7+ from https://python.org"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo

# Install requirements
echo "📦 Installing required packages..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install requirements"
    exit 1
fi

echo "✅ Packages installed successfully"
echo

# Create contacts directory
mkdir -p contacts
echo "✅ Contacts directory ready"
echo

echo "🚀 Starting the portfolio server..."
echo "📍 Your portfolio will be available at: http://localhost:5000"
echo "🌐 Network access: http://0.0.0.0:5000"
echo "📧 Contact API: http://localhost:5000/api/contact"
echo "💚 Health check: http://localhost:5000/api/health"
echo
echo "💡 Press Ctrl+C to stop the server"
echo "=================================================="
echo

# Start the Flask application
python3 app.py
