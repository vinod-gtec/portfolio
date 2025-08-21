#!/usr/bin/env python3
"""
Simple script to run the Vinod Kumar Portfolio Flask application
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def install_requirements():
    """Install required packages if not already installed"""
    try:
        import flask
        print("✅ Flask is already installed")
    except ImportError:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully")

def create_contacts_directory():
    """Create contacts directory if it doesn't exist"""
    if not os.path.exists('contacts'):
        os.makedirs('contacts')
        print("✅ Created contacts directory")

def main():
    """Main function to run the portfolio server"""
    print("🎯 Vinod Kumar Portfolio - Flask Backend")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Install requirements
    install_requirements()
    
    # Create necessary directories
    create_contacts_directory()
    
    print("\n🚀 Starting the portfolio server...")
    print("📍 Your portfolio will be available at: http://localhost:5000")
    print("🌐 Network access: http://0.0.0.0:5000")
    print("📧 Contact API: http://localhost:5000/api/contact")
    print("💚 Health check: http://localhost:5000/api/health")
    print("\n💡 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Import and run the Flask app
    from app import app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

if __name__ == '__main__':
    main()
