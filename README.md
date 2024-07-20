http://ec2-3-19-67-200.us-east-2.compute.amazonaws.com:8000/api/tasks/

# Todo Backend

This is the backend for the Todo application, built with Django and deployed on an AWS EC2 instance.

## Tech Stack

- **Backend Framework:** Django 3.2.25
- **Database:** SQLite (default)
- **Server:** Nginx and Gunicorn
- **Deployment:** AWS EC2
- **Other Dependencies:** Django REST framework, django-cors-headers

## Project Setup

### Prerequisites

- Python 3.x
- pip
- virtualenv
- AWS account
- SSH access to an AWS EC2 instance

### Installation

1. **Clone the repository:**
   
   git clone [https://github.com/yourusername/todo-backend.git](https://github.com/JibonP/todo-backend.git)
   cd todo-backend
Create a virtual environment:


python3 -m venv venv
source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Run migrations:


python manage.py migrate
Start the development server:


python manage.py runserver
Deployment
Launch an EC2 instance and SSH into it:


ssh -i /path/to/your-key.pem ubuntu@your-ec2-public-dns
Install required packages:


sudo apt update
sudo apt install -y python3 python3-venv python3-pip nginx git
Clone the repository and set up the project:


git clone [https://github.com/yourusername/todo-backend.git](https://github.com/JibonP/todo-backend.git)
cd todo-backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run migrations:


python manage.py migrate
Set up Gunicorn:

Create a systemd service file for Gunicorn:


sudo nano /etc/systemd/system/gunicorn.service




Start and enable Gunicorn:

bash
Copy code
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
Configure Nginx:

Create an Nginx configuration file:

nginx

sudo nano /etc/nginx/sites-available/todo-backend

server {
    listen 80;
    server_name your-ec2-public-dns;

    location / {
        proxy_pass http://unix:/home/ubuntu/todo-backend/gunicorn.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
Enable the configuration and restart Nginx:

```
sudo ln -s /etc/nginx/sites-available/todo-backend /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
API Endpoints
List Tasks: GET /api/tasks/
Create Task: POST /api/tasks/
Update Task: PUT /api/tasks/:id/
Delete Task: DELETE /api/tasks/:id/
```
