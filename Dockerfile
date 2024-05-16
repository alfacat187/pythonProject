FROM python:3.10-alpine
LABEL authors="alexander"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN chmod 755 .
COPY webhook1.py webhook.py

