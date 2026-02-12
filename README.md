# 📚 HomeLibrary

🚀 A modern Flask-based web application for managing your personal book library with Google OAuth authentication.

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1+-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🔐 **Google OAuth Authentication** - Secure login with Google accounts
- 📚 **Book Management** - Add, edit, delete, and search your book collection
- 🌐 **RESTful API** - Clean and well-documented API endpoints
- 🐳 **Docker Support** - Easy deployment with Docker Compose
- 📊 **Database Migrations** - Schema management with Alembic
- 🎨 **Modern UI** - Responsive web interface
- ⚡ **Fast Performance** - Optimized for speed and efficiency
- 🛡️ **Secure** - Built with security best practices

## 🚀 Quick Start

### 📋 Prerequisites

- 🐍 Python 3.13 or higher
- 🐘 PostgreSQL database
- 🔑 Google OAuth 2.0 credentials

### 🛠️ Installation

1. **📥 Clone the repository**
   ```bash
   git clone <repository-url>
   cd HomeLibrary
   ```

2. **🔧 Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **📦 Install dependencies**
   ```bash
   pip install -e .
   ```

4. **⚙️ Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **🚀 Run the application**
   ```bash
   python app.py
   ```

Visit `http://localhost:5000` to access the application. 🎉

## ⚙️ Configuration

### 🔐 Environment Variables

Create a `.env` file with the following variables:

```env
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/homelibrary
DEBUG=True

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Security
SECRET_KEY=your-secret-key-here
```

### 🔑 Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URI: `http://localhost:5000/auth/callback`
6. Copy credentials to your `.env` file

## 📚 API Documentation

### 🔐 Authentication Endpoints

- `GET /auth/login` - Initiate Google OAuth login
- `GET /auth/callback` - OAuth callback handler
- `GET /auth/logout` - Logout user
- `GET /profile` - User profile (requires authentication)

### 📖 Books API

- `GET /api/books` - Get all books
- `GET /api/books/<id>` - Get a specific book
- `POST /api/books` - Create a new book
- `PUT /api/books/<id>` - Update a book
- `DELETE /api/books/<id>` - Delete a book

### 💡 Example API Usage

```bash
# Get all books
curl -X GET http://localhost:5000/api/books

# Create a new book
curl -X POST http://localhost:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}'
```

## 📁 Project Structure

```
HomeLibrary/
├── api/                 # API routes and handlers
│   └── routers/
│       └── books.py     # Book-related API endpoints
├── auth/                # Authentication logic
│   ├── google_auth.py   # Google OAuth implementation
│   ├── login_manager.py # Flask-Login configuration
│   └── routes.py        # Authentication routes
├── crud/                # Database operations
├── database/            # Database configuration
│   ├── config.py        # Database settings
│   └── database.py      # Database connection
├── exceptions/          # Custom exceptions
├── migrations/          # Database migrations
├── models/              # Database models
│   ├── book.py          # Book model
│   └── user.py          # User model
├── schemas/             # Data validation schemas
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── utils/               # Utility functions
├── app.py              # Main application entry point
├── alembic.ini         # Alembic configuration
├── docker-compose.yml  # Docker Compose configuration
├── dockerfile          # Docker configuration
├── dockerignore        # Docker ignore file
├── gitignore           # Git ignore file
├── pyproject.toml      # Project dependencies
├── requirements.txt    # Pip dependencies
├── env.example        # Example environment variables
├── QUICK_START.md      # Quick start guide
├── README.md           # This file
└── LICENSE             # MIT License
```

## 👨‍💻 Development

### ✅ Code Quality

The project uses Ruff for linting and formatting:

```bash
# Check code quality
ruff check .

# Format code
ruff format .
```

### 🗄️ Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migration
alembic upgrade head
```

### 🐳 Docker Development

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in background
docker-compose up -d

# Stop containers
docker-compose down
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📝 Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Use meaningful commit messages
- Keep the codebase clean and organized

## 🧪 Testing

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=.

# Run specific test file
python -m pytest tests/test_books.py
```

## 🚀 Deployment

### 🏭 Production Setup

1. Set environment variables:
   ```env
   DEBUG=False
   DATABASE_URL=postgresql://user:pass@prod-db:5432/homelibrary
   ```

2. Use a production WSGI server:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. Set up reverse proxy (nginx/Apache)
4. Configure SSL certificates
5. Set up monitoring and logging

### 🐳 Docker Production

```bash
# Build production image
docker build -t homelibrary:latest .

# Run with production settings
docker run -d -p 5000:5000 --env-file .env homelibrary:latest
```

## 🔧 Troubleshooting

### ⚠️ Common Issues

**🗄️ Database Connection Error**
- Ensure PostgreSQL is running
- Check DATABASE_URL in `.env`
- Verify database exists

**🔑 Google OAuth Error**
- Verify Client ID and Secret
- Check redirect URI in Google Console
- Ensure Google+ API is enabled

**🚪 Port Already in Use**
- Change port in `app.py`
- Kill process using port 5000

## 🗺️ Roadmap

- [ ] 📸 Add book cover image uploads
- [ ] ⭐ Implement book ratings and reviews
- [ ] 📈 Add reading progress tracking
- [ ] 🤖 Book recommendations based on reading history
- [ ] 📤 Export/import library data
- [ ] 🔗 Integration with Goodreads API

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🌟 Flask framework and its ecosystem
- 🔐 Google OAuth 2.0 documentation
- 🐘 PostgreSQL database
- 🌍 The open-source community

---

# 📚 Happy Reading! Enjoy your personal library! 🎉