# syntax=docker/dockerfile:1

FROM python:3.12-slim-bullseye

LABEL "maintainer" "Noel <noel@anorak.dev>"
LABEL "repository" "https://github.com/anor4k/action-python-autotagging"
LABEL "homepage" "https://github.com/anor4k/action-python-autotagging"


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY main.py /app/main.py

CMD [ "python3", "/app/main.py" ]
