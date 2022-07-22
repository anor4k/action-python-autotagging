# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
WORKDIR /github/workspace

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py main.py

CMD [ "python3", "/github/workspace/main.py" ]
