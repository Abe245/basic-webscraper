FROM python:3.10-slim-buster
RUN mkdir /home/app
WORKDIR /home/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app .
