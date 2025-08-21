# 🚀 Vinod Kumar Portfolio - Flask Backend Setup Guide

This guide will help you set up and run your portfolio website with a Flask backend.

## 📋 Prerequisites

- **Python 3.7 or higher** installed on your system
- **pip** (Python package installer)
- **Git** (optional, for version control)

## 🛠️ Installation & Setup

### Option 1: Quick Start (Recommended)

#### Windows Users:
1. Double-click `start.bat`
2. The script will automatically:
   - Check Python installation
   - Install required packages
   - Start the server

#### Linux/Mac Users:
1. Open terminal in the project directory
2. Make the script executable: `chmod +x start.sh`
3. Run: `./start.sh`

### Option 2: Manual Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Alternative: Use the run script:**
   ```bash
   python run.py
   ```

## 🌐 Accessing Your Portfolio

Once the server is running, you can access your portfolio at:

- **Local access:** http://localhost:5000
- **Network access:** http://0.0.0.0:5000
- **Contact API:** http://localhost:5000/api/contact
- **Health check:** http://localhost:5000/api/health

## 📧 Email Configuration (Optional)

To enable email notifications when someone submits the contact form:

### 1. Gmail Setup
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"

### 2. Update Configuration
Edit `app.py` and update these lines:
```python
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Your Gmail
app.config['MAIL_PASSWORD'] = 'your-app-password'     # Generated app password
```

### 3. Enable Email Notifications
In `app.py`, uncomment this line:
```python
# send_email_notification(contact_data)  # Remove the # to enable
```

## 📁 File Structure

```
portfolio/
├── index.html          # Main portfolio page
├── styles.css          # CSS styles and animations
├── script.js           # Frontend JavaScript
├── app.py              # Flask backend application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── run.py              # Alternative run script
├── start.bat           # Windows startup script
├── start.sh            # Linux/Mac startup script
├── contacts/           # Contact form submissions (auto-created)
├── README.md           # Portfolio documentation
└── SETUP.md            # This setup guide
```

## 🔧 Configuration Options

### Environment Variables (Production)
For production deployment, use environment variables:

```bash
export MAIL_USERNAME="your-email@gmail.com"
export MAIL_PASSWORD="your-app-password"
export SECRET_KEY="your-secret-key"
```

### Customizing the Portfolio
1. **Personal Information:** Edit `index.html`
2. **Styling:** Modify `styles.css`
3. **Functionality:** Update `script.js`
4. **Backend Logic:** Customize `app.py`

## 🚀 Deployment Options

### 1. Local Development
- Perfect for testing and development
- Accessible only on your machine

### 2. Local Network
- Share with others on your network
- Accessible at your computer's IP address

### 3. Production Deployment
Recommended platforms:
- **Heroku:** Easy deployment with Git
- **PythonAnywhere:** Free Python hosting
- **DigitalOcean:** VPS hosting
- **AWS/GCP:** Cloud hosting

## 🔍 Troubleshooting

### Common Issues:

1. **Port 5000 already in use:**
   ```bash
   # Find and kill the process
   lsof -ti:5000 | xargs kill -9
   # Or change port in app.py
   ```

2. **Python not found:**
   - Install Python from https://python.org
   - Ensure Python is in your PATH

3. **Package installation fails:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Email not working:**
   - Check Gmail app password
   - Ensure 2FA is enabled
   - Verify email configuration

### Getting Help:
- Check the console output for error messages
- Verify all files are in the same directory
- Ensure Python 3.7+ is installed

## 📊 Features

### ✅ What's Included:
- **Static File Serving:** HTML, CSS, JS files
- **Contact Form API:** Handles form submissions
- **Email Notifications:** Optional Gmail integration
- **File Storage:** Saves contacts locally
- **Health Check:** API endpoint for monitoring
- **Error Handling:** Proper error responses
- **CORS Support:** Cross-origin requests
- **Validation:** Form and email validation

### 🔄 API Endpoints:
- `GET /` - Main portfolio page
- `POST /api/contact` - Contact form submission
- `GET /api/health` - Health check
- `GET /<filename>` - Static file serving

## 🎯 Next Steps

1. **Customize Content:** Update your information in `index.html`
2. **Add Projects:** Include your actual project details
3. **Configure Email:** Set up email notifications
4. **Deploy:** Choose a hosting platform
5. **Domain:** Add a custom domain name

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Verify your Python installation
3. Review the console output
4. Ensure all files are present

---

**🎉 Your portfolio is now ready to showcase your AI and Data Analytics expertise!**
