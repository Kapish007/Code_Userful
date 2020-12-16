https://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/


sudo apt-get update
sudo apt-get upgrade

# PROJECT NAME = Glammer_project_dev
sudo nano /etc/nginx/sites-available/Glammer_project_dev

# =========================================================================================
server {
    listen 8000;
    server_name 0.0.0.0;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
            root /home/ubuntu/Glammer_project_dev/Glammer_Project;
    }

    location / {
            include proxy_params;
            proxy_pass http://unix:/home/ubuntu/Glammer_project_dev/Glammer_Project/Glammer_Project.sock;
    }
}
# =========================================================================================
sudo ln -s /etc/nginx/sites-available/Glammer_project_dev /etc/nginx/sites-enabled
sudo nginx -t

include /etc/nginx/sites-enabled/*

sudo nano /etc/supervisor/conf.d/Glammer_project_dev.conf

# =========================================================================================
[program:Glammer_project_dev]
command=/home/ubuntu/.local/bin/gunicorn --timeout 600 -w 2 --bind unix:/home/ubuntu/Glammer_project_dev/Glammer_Project/Glammer_Project.sock Glammer_Project.wsgi
directory=/home/ubuntu/Glammer_project_dev/Glammer_Project
user=ubuntu
autostart=true
autorestart=true
stderr_logfile=/var/log/Glammer_project_dev.err.log
#stdout_logfile=/var/log/Glammer_project_dev.out.log

# =========================================================================================



sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status Glammer_project_dev

sudo service nginx restart && sudo supervisorctl restart Glammer_project_dev