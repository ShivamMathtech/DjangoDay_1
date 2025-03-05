# Django User Registration Project

## Overview

This is a simple Django application that allows users to input their username and password through an HTML form and saves the data in the Django admin panel.

## Features

- User registration with username and password
- Form validation using Django Forms
- Data storage in the Django database
- Admin panel integration to manage users

## Technologies Used

- Django
- HTML/CSS
- SQLite (default Django database)

## Installation

### 1. Clone the Repository

```bash
https://github.com/yourusername/django-user-registration.git
cd django-user-registration
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (To Access Admin Panel)

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username and password.

### 6. Run the Server

```bash
python manage.py runserver
```

### 7. Access the Application

- Open the browser and go to: `http://127.0.0.1:8000/register/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
user_management/
│── users/
│   ├── migrations/
│   ├── templates/
│   │   ├── users/
│   │   │   ├── form.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│── user_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── manage.py
│── requirements.txt
│── README.md
```

## Usage

1. Fill in the username and password in the form.
2. Submit the form.
3. The data will be stored in the Django database.
4. Admins can log in and manage users in the Django admin panel.

## Troubleshooting

- If changes to static files (CSS/JS) are not reflecting, try:
  ```bash
  python manage.py collectstatic --noinput
  ```
- If you face any database migration issues, try:
  ```bash
  python manage.py migrate --run-syncdb
  ```

## License

This project is open-source and available under the MIT License.

## Author

Shivam Singh
