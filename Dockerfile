# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

LABEL "maintainer" "Jorrick Sleijster <jorrick3@gmail.com>"
LABEL "repository" "https://github.com/Jorricks/action-autotag-python"
LABEL "homepage" "https://github.com/Jorricks/action-autotag-python"


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY main.py /app/main.py

CMD [ "python3", "/app/main.py" ]
