FROM python:3.7
LABEL maintainer="Paul Schifferer <paul@schifferers.net>"

RUN apt-get update && apt-get install -y wget

RUN groupadd survey && useradd -d /app -m -g survey survey
COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt
# # TODO: remove [start]
# RUN python manage.py db init
# RUN python manage.py db migrate
# # TODO: remove [end]
# RUN python manage.py db upgrade

USER survey:survey
EXPOSE 5000
ENTRYPOINT [ "uwsgi", "--ini", "/app/surveyapi.ini" ]
