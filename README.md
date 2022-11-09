Test task ToDo on Django Rest Framework
---------------------------------------

Installation
---------

##### Clone a repository
```
https://github.com/vadushkin/DjangoRestToDo.git
```

##### Change a folder
```
cd ...
```

##### Virtual venv
```
python -m venv venv
```

##### Activate
```
.\venv\Scripts\activate
```

##### Install requirements
```
poetry install
poetry shell
```

##### Migrate
```
python manage.py migrate
```

#### Create file `.env`

#### Fill in the data in the file `.env`

### Example:

```dotenv
SECRET_KEY=
DEBUG=

MYSQL_ENGINE=
MYSQL_NAME=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=

EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=
EMAIL_USE_SSL=
```

##### Run
```
python manage.py runserver
```

##### Admin Panel

```
python manage.py createsuperuser
```

[//]: # (Docker)

[//]: # (------)

[//]: # ()
[//]: # (```)

[//]: # (https://github.com/vadushkin/DjangoRestToDo.git)

[//]: # (cd ...)

[//]: # (docker-compose up -d)

[//]: # (```)

[//]: # ()
[//]: # (### Stop Docker)

[//]: # (```)

[//]: # (docker-compose stop)

[//]: # (```)

Api
------

* `admin/` 

#### To-do:

* `to-do/` 
* `to-do/boards-list/`
* `to-do/board-create/`
* `to-do/board-upd-del/int:pk/`
* `to-do/todo-create/`
* `to-do/todo-list/int:pk/`
* `to-do/todo-update/int:pk/`
* `to-do/todo-delete/int:pk/`
* `to-do/todo-list-undone/int:pk/`


* `to-do/swagger/`
* `to-do/redoc/`

#### Mention:

* `mention/`
* `mention/reminder-list/`
* `mention/reminder-create/`
* `mention/reminder-delete/int:pk/`