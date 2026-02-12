# Quick Start Guide

## Overview

HomeLibrary is a Flask-based web application for managing your personal book library with Google OAuth authentication. The application uses PostgreSQL as the database and provides a RESTful API for book management.

## Prerequisites

- Python 3.13 or higher
- PostgreSQL database
- Google OAuth 2.0 credentials (for authentication)
- Docker and Docker Compose (optional, for containerized deployment)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd HomeLibrary
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -e .
```

Or using uv (if available):

```bash
uv sync
```

## Configuration

### 1. Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/homelibrary
DEBUG=True

# Google OAuth Configuration
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Application Security
SECRET_KEY=your-secret-key-here
```

### 2. Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URI: `http://localhost:5000/auth/callback`
6. Copy the Client ID and Client Secret to your `.env` file

### 3. Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE homelibrary;
```

## Running the Application

### Method 1: Direct Python Execution

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Method 2: Using Docker Compose

```bash
docker-compose up --build
```

## Database Migrations

The application uses Alembic for database migrations.

### Initialize Migrations

```bash
alembic init alembic
```

### Create Migration

```bash
alembic revision --autogenerate -m "Initial migration"
```

### Apply Migration

```bash
alembic upgrade head
```

## API Endpoints

### Authentication

- `GET /auth/login` - Initiate Google OAuth login
- `GET /auth/callback` - OAuth callback handler
- `GET /auth/logout` - Logout user
- `GET /profile` - User profile (requires authentication)

### Books API

- `GET /api/books` - Get all books
- `GET /api/books/<id>` - Get a specific book
- `POST /api/books` - Create a new book
- `PUT /api/books/<id>` - Update a book
- `DELETE /api/books/<id>` - Delete a book

## Project Structure

```
HomeLibrary/
├── api/                 # API routes and handlers
├── auth/                # Authentication logic
├── crud/                # Database operations
├── database/            # Database configuration
├── exceptions/          # Custom exceptions
├── migrations/          # Database migrations
├── models/              # Database models
├── schemas/             # Data validation schemas
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── utils/               # Utility functions
├── app.py              # Main application entry point
├── alembic.ini         # Alembic configuration
├── docker-compose.yml  # Docker Compose configuration
└── pyproject.toml      # Project dependencies and configuration
```

## Development

### Code Quality

The project uses Ruff for linting and formatting:

```bash
# Check code quality
ruff check .

# Format code
ruff format .
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=.
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Check DATABASE_URL in `.env` file
   - Verify database exists

2. **Google OAuth Error**
   - Verify Client ID and Secret are correct
   - Check redirect URI in Google Console matches your application
   - Ensure Google+ API is enabled

3. **Port Already in Use**
   - Change port in `app.py` or kill the process using port 5000

### Logs

Check the application logs for detailed error information. The application prints database connection status and table creation messages on startup.

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Use a production-grade WSGI server like Gunicorn
3. Configure proper database connection pooling
4. Set up proper logging
5. Use HTTPS for OAuth callbacks

Example production command:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

Add your license information here.
