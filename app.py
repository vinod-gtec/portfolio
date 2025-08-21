from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'your-app-password'     # Update with your app password

# Ensure static files are served correctly
app.static_folder = '.'
app.static_url_path = ''

@app.route('/')
def index():
    """Serve the main portfolio page"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve static files (CSS, JS, images)"""
    return send_from_directory('.', filename)

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        # Email validation
        import re
        email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_pattern, data['email']):
            return jsonify({'error': 'Invalid email format'}), 400
        
        # Save to file (simple storage)
        contact_data = {
            'name': data['name'],
            'email': data['email'],
            'subject': data['subject'],
            'message': data['message'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Create contacts directory if it doesn't exist
        os.makedirs('contacts', exist_ok=True)
        
        # Save contact to file
        filename = f"contacts/contact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(contact_data, f, indent=2)
        
        # Optional: Send email notification
        # send_email_notification(contact_data)
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        })
        
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing your request'}), 500

def send_email_notification(contact_data):
    """Send email notification when contact form is submitted"""
    try:
        msg = MIMEMultipart()
        msg['From'] = app.config['MAIL_USERNAME']
        msg['To'] = app.config['MAIL_USERNAME']  # Send to yourself
        msg['Subject'] = f"New Portfolio Contact: {contact_data['subject']}"
        
        body = f"""
        New contact form submission:
        
        Name: {contact_data['name']}
        Email: {contact_data['email']}
        Subject: {contact_data['subject']}
        Message: {contact_data['message']}
        Time: {contact_data['timestamp']}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
        server.starttls()
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        text = msg.as_string()
        server.sendmail(app.config['MAIL_USERNAME'], app.config['MAIL_USERNAME'], text)
        server.quit()
        
    except Exception as e:
        print(f"Email notification failed: {e}")

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Vinod Kumar Portfolio'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Development server
    print("🚀 Starting Vinod Kumar Portfolio Server...")
    print("📍 Local: http://localhost:5000")
    print("🌐 Network: http://0.0.0.0:5000")
    print("📧 Contact form API: http://localhost:5000/api/contact")
    print("💚 Health check: http://localhost:5000/api/health")
    print("\n✨ Portfolio is ready!")
    print("📝 To enable email notifications, update the email configuration in app.py")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
