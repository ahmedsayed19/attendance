# Attendance App

it's a web app to help employers know how much time any employee has worked moreover when he checks in and out.

## Run the app locally

create a virtual enviroment 
```
python -m venv env
``` 

install requirements
```
pip install -r requirements.txt
```

make database migrations
```
python manage.py makemigrations
python manage.py migrate
```

create a super user to be able to interact with a dashboard
```
python manage.py createsuperuser
```

and finally run the server to see the app on http://127.0.0.1:8000
```
python manage.py runserver
```



