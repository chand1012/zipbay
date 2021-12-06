# Running

Requires [Python 3.6](https://www.python.org/downloads/) or greater. After it is installed, open a new terminal in the project directory and execute the following commands.

```
pip install pipenv
pipenv install
pipenv shell
cd zipbay
python manage.py migrate
python manage.py runserver 8080
```

To create a new admin user that can access the admin panel, first stop the server. Then execute the following.

```
python manage.py createsuperuser
```

The user you create can now access the admin panel found at `localhost:8080/admin` after restarting the server.
