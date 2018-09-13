FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
RUN mkdir /code
WORKDIR /code
ADD Pipfile Pipfile.lock /code/
#  RUN pipenv lock -r > requirements.txt && pip install -r requirements.txt
RUN apk update && \
 apk add postgresql-libs gettext && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pipenv install --system --deploy && \
 apk --purge del .build-deps
ADD . /code/
RUN python manage.py compilemessages
