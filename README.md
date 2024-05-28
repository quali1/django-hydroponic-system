# Hydroponic System Manager

## Introduction

This project is a Django-based application for managing a hydroponic system. The application is configured to work with a PostgreSQL database and can be easily deployed using Docker.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/quali1/django-hydroponic-system
    cd django-hydroponic-system
    ```
   
2. **Build and Start the Containers**

   Docker Compose will manage the database and web server containers for you. In the root directory of the project, run the following commands:
    ```bash
   docker-compose up --build
   ```
   
3. **Apply Database Migrations**
   
   After the containers are up and running, apply the database migrations to initialize the database schema:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a Superuser**

   Create a superuser to access the Django admin panel:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   
5. **Access the Application**

   Open your browser and go to http://localhost:8000 to access the application.