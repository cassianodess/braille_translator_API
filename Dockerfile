# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

SHELL ["/bin/bash", "-c"]

RUN apt update -y && apt upgrade -y && apt install apt-transport-https -y && apt install make -y

RUN apt install tesseract-ocr -y && apt install libtesseract-dev -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "make", "run"]