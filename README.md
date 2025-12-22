BlogSphere - Professional Blogging Platform<br>
A full-featured, modern blogging platform built with Django that allows users to create, manage, and share blog posts with an elegant, responsive interface.

🌟 Live Demo
Visit the live application: https://blogsphere-tj47.onrender.com/

Admin Panel: https://blogsphere-tj47.onrender.com//admin/

✨ Features
🔐 User Authentication
User registration with email verification

Secure login/logout system

Password reset functionality

User profile management

📝 Content Management
Create, edit, and delete blog posts

Rich text editing with real-time preview

Category-based post organization

Featured image upload with Cloudinary integration

Draft saving and auto-save functionality

🎨 Modern UI/UX
Responsive design (mobile-first approach)

Clean, professional interface with gradient accents

Smooth animations and transitions


🔧 Technical Features
PostgreSQL database (production)

Cloudinary for image storage

Whitenoise for static files

Gunicorn for production server

Environment-based configuration

CSRF protection and security best practices

📊 User Dashboard
Personal post management

View all created posts

Edit/Delete functionality

Post statistics and analytics

🛠️ Technology Stack
Backend
Framework: Django 5.2.5

Database: PostgreSQL (Production), SQLite (Development)

Authentication: Django Auth System

API: Django REST Framework ready

Frontend
HTML5, CSS3, JavaScript

Bootstrap 5.3 for responsive design

Font Awesome 6 for icons

Custom CSS with CSS variables

Third-party Services
Cloudinary - Image and media storage

Render - Deployment and hosting

Gunicorn - WSGI HTTP server

Whitenoise - Static file serving

Development Tools
Git for version control

GitHub for repository hosting

Pip for dependency management

Virtual Environment for isolation

🚀 Quick Start
Prerequisites
Python 3.10 or higher

pip (Python package manager)

Git

PostgreSQL (for production)

Installation
Clone the repository

git clone https://github.com/yourusername/blogsphere.git
cd blogsphere
Create virtual environment

python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Configure environment variables

cp .env.example .env
# Edit .env file with your settings
Run migrations

python manage.py migrate
Create superuser

python manage.py createsuperuser
Run development server

python manage.py runserver
