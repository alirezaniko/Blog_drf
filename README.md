# Blog Project

This is a Django-powered blog application that allows users to create and share articles, comment on posts, and categorize content. The app supports user authentication, CRUD operations for articles, and a hierarchical commenting system.

## Features
- **User Authentication**: Register, login, and logout functionality for users.
- **Article Management**: Users can create, read, update, and delete articles with support for categories and unique slugs.
- **Comment System**: Users can comment on articles and reply to other comments.
- **Category Filter**: Browse articles by categories for easier content discovery.
- **Search**: Full-text search functionality for articles.
- **Admin Management**: Django admin integration for managing users, articles, and comments.

## API Endpoints
- `/api/articles/` - List and manage articles
- `/api/categories/` - List categories and associated articles
- `/api/comments/` - Manage comments on articles
- `/api/auth/` - User registration and authentication endpoints

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blog.git
   cd blog
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations and start the server:
   ``` bash
   python manage.py migrate
   python manage.py runserver
   ```
   Access the application at http://localhost:8000.

   
Replace `https://github.com/yourusername/blog.git` with your actual GitHub repository link. Adjust any sections to include additional details specific to your project!
