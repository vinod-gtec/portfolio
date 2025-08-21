@echo off
echo 🎯 Vinod Kumar Portfolio - Flask Backend
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Install requirements
echo 📦 Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Error: Failed to install requirements
    pause
    exit /b 1
)

echo ✅ Packages installed successfully
echo.

REM Create contacts directory
if not exist "contacts" mkdir contacts
echo ✅ Contacts directory ready
echo.

echo 🚀 Starting the portfolio server...
echo 📍 Your portfolio will be available at: http://localhost:5000
echo 🌐 Network access: http://0.0.0.0:5000
echo 📧 Contact API: http://localhost:5000/api/contact
echo 💚 Health check: http://localhost:5000/api/health
echo.
echo 💡 Press Ctrl+C to stop the server
echo ==================================================
echo.

REM Start the Flask application
python app.py

pause
