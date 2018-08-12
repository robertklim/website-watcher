FROM python:3.7.0-slim-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/website-watcher/src
ADD src/requirements.txt /usr/src/website-watcher/src/
RUN pip install -r requirements.txt