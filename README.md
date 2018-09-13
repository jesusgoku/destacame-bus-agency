# Destacame: Bus Agency

Backend para gestionar una agencia de buses.

- Permite crear y gestionar **Buses**, **Conductores**, y **Rutas**.
- Cada `Ruta` tiene **Viajes** en diferentes horarios.
- Cada `Viaje` tiene una **capacidad de pasajeros** de acuerdo a la capacidad del `Bus` seleccionado para este.
- Validación de disponibilidad del `Bus` al crear el `Viaje`.
- Validación de disponibilidad del `Conductor` al crear el `Viaje`.
- Validación de la duración minima del `Viaje`.
- Validación de la capacidad del `Viaje -> Bus`.
- Validación de la sobre-venta de asiento.
- Obtener `Conductores` disponibles para un horario.
- Obtener `Buses` disponibles para un horario.
- Gestión desde Django admin.
- Gestión desde API REST.


## Requirements

- Python 3.6
- Postgres 9.6
- Pipenv

### Optionals

- Gettext (for compile translations)
- Docker (for running easy)

## Running local

```shell
cp .env.dist .env
vim .env # Complete with DB info
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py loaddata db.json
pipenv run python manage.py compilemessages # Skip for not translations
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

## TODO

- Testing
- API Documentation
- API Authentication
- Frontend
