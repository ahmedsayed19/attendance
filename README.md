# Attendance App

It's a web app to help employers know how much time any employee has worked moreover when he checks in and out.

## How this app work

It has two route:
- ```employees/<str:employee>/dates/<str:date>```

    It takes two params: 
    employee like EMP03 date like 2023-01-05 and it returns.

    ```
    {
        “attended”: true,
        “duration”: “12:00”
    }
    ```
    Duration is the time employee worked that day

- ```employees/<str:employee>```
    it returns json like that
    ```
    {
        “days”: [
            {
                “date”: “2020-04-03”
                “actions”: [
                    { 
                        “action”: “CheckOut”, 
                        “time”: “2020-04-01T10:05:00.000000+00:00” 
                    },
                ]
            },
        ]
    }

    ```

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

Add enviroment variables file .env and and add these two variables with tese test values
```
SECRET_KEY=django-insecure-ct^ue2m!soa=t=x8)l@a8-$uo1za^j_2@4h8ajz%z1&it8ys6r
DEBUG=1
```

and finally run the server to see the app on http://127.0.0.1:8000
```
python manage.py runserver
```



