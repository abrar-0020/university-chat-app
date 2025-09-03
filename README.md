# 🎓 University Chat System

A real-time chat application designed for university students with secure authentication and cross-device synchronization.

![Chat Demo](https://img.shields.io/badge/Real--time-Chat-blue) ![University](https://img.shields.io/badge/University-Students-green) ![Free](https://img.shields.io/badge/Deploy-Free-orange)

## ✨ Features

- 🔐 **Secure Authentication**: University email validation (@university.edu)
- 💬 **Real-time Messaging**: Instant message delivery with Socket.IO
- 📱 **Cross-Device**: Works on desktop, tablet, and mobile
- 🔒 **Password Security**: Bcrypt hashing for user passwords
- 🌐 **Web-based**: No app installation required
- ⚡ **Fast & Responsive**: Modern React interface with Tailwind CSS

## 🚀 Live Demo

**[🌐 Try it live here!]** *(Add your deployed URL)*

## 🛠️ Tech Stack

- **Backend**: Python Flask + Flask-SocketIO
- **Frontend**: React (served from backend)
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Real-time**: Socket.IO WebSockets
- **Styling**: Tailwind CSS
- **Deployment**: Render/Railway/Heroku compatible

## 📋 Quick Start

### Local Development
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/university-chat-app.git
cd university-chat-app

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open in browser
http://localhost:5000
```

### Deploy to Cloud (Free)
1. **Fork this repository**
2. **Deploy to [Render](https://render.com)** (recommended)
3. **Configure**: Python 3.11, auto-deploy from GitHub
4. **Share your live URL!**

*See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.*

## 🎯 How to Use

1. **Register** with your university email (must end with @university.edu)
2. **Login** to access the chat room
3. **Send messages** - they appear instantly on all connected devices
4. **Cross-device sync** - login from phone and laptop simultaneously!

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key (auto-generated if not set)
- `PORT`: Server port (auto-configured by hosting platform)

### Email Validation
Currently accepts emails ending with `@university.edu`. To change this:
```python
# In app.py, line 35
if not email.endswith("@university.edu"):
    # Change to your university domain
```

## 📱 Mobile Friendly

The app is fully responsive and works great on:
- 📱 Mobile phones
- 📟 Tablets  
- 💻 Desktop computers
- 🖥️ Any device with a web browser

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

Having issues? 
- Check the [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- Open an issue on GitHub
- Contact: [Your contact info]

---

**Made with ❤️ for university students everywhere!**

*Star ⭐ this repo if you found it helpful!*
