# Destacame: Bus Agency

## Requirements

- Python 3.6
- Postgres 9.6
- Pipenv
- Gettext (For compile translations)

## Running local

```shell
cp .env.dist .env
vim .env # Complete with DB info
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py loaddata db.json
pipenv run python manage.py compilemessages
pipenv run python manage.py runserver
# Open your browser on: http://localhost:8000
```

## Running on Docker

Project allow run on docker containers

```shell
# Run only first mount app
docker-compose run app python manage.py migrate
docker-compose run app python manage.py loaddata db.json

# Run every up app
docker-compose up

# Open your browser on: http://localhost:8000
```
