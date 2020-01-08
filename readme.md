# 50CS

## Install dependencies with pipenv

These instructions assume that you have already installed pipenv.
All you need to do is cd into 5OCS and run

```bash
pipenv install
```

## Run the server and see if its 5

First activate the virtual environment with:

```bash
pipenv shell
```

Then launch the server with:

```bash
python3 manage.py runserver
```

Finally, open your browser and go to http://127.0.0.1:8000/isitfiveyet
