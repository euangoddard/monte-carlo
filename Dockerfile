FROM python:3.11-slim

WORKDIR /opt/monty

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/opt/monty