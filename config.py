"""
Configuration file for Vinod Kumar Portfolio Flask Application
"""

import os
from datetime import datetime

class Config:
    """Base configuration class"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    DEBUG = True
    
    # Email Configuration (Gmail)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    
    # Update these with your email credentials
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'your-email@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'your-app-password'
    
    # Portfolio Information
    PORTFOLIO_NAME = "Vinod Kumar"
    PORTFOLIO_TITLE = "AI & Data Analytics Specialist"
    PORTFOLIO_DESCRIPTION = "Passionate about leveraging artificial intelligence and data analytics to solve real-world problems."
    
    # Contact Information
    CONTACT_EMAIL = "vinod.kumar@example.com"
    CONTACT_PHONE = "+91 98765 43210"
    CONTACT_LOCATION = "Chennai, Tamil Nadu, India"
    LINKEDIN_URL = "linkedin.com/in/vinodkumar"
    
    # File Storage
    CONTACTS_DIR = "contacts"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # API Configuration
    API_RATE_LIMIT = "100 per minute"
    
    @staticmethod
    def init_app(app):
        """Initialize application with configuration"""
        # Create necessary directories
        os.makedirs(Config.CONTACTS_DIR, exist_ok=True)
        
        # Log configuration
        print(f"📧 Email notifications: {'Enabled' if Config.MAIL_USERNAME != 'your-email@gmail.com' else 'Disabled'}")
        print(f"🔐 Secret key: {'Custom' if os.environ.get('SECRET_KEY') else 'Default'}")
        print(f"📁 Contacts directory: {Config.CONTACTS_DIR}")

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # Use environment variables for production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# Email setup instructions
EMAIL_SETUP_INSTRUCTIONS = """
📧 Email Setup Instructions:

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security > 2-Step Verification > App passwords
   - Generate a new app password for "Mail"
3. Update the configuration:
   - Set MAIL_USERNAME to your Gmail address
   - Set MAIL_PASSWORD to the generated app password
4. Uncomment the email notification line in app.py

For production, use environment variables:
export MAIL_USERNAME="your-email@gmail.com"
export MAIL_PASSWORD="your-app-password"
export SECRET_KEY="your-secret-key"
"""
