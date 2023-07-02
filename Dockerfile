# syntax=docker/dockerfile:1

FROM python:3.11-buster

SHELL ["/bin/bash", "-c"]

RUN apt update -y && apt upgrade -y && apt install apt-transport-https -y && apt install make -y

RUN apt-get install automake ca-certificates g++ git libtool libleptonica-dev make pkg-config -y

RUN apt-get install --no-install-recommends asciidoc docbook-xsl xsltproc -y

RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN apt-get install libpango1.0-dev -y

RUN git clone https://github.com/tesseract-ocr/tesseract.git

RUN cd tesseract && ./autogen.sh && ./configure && make && make install && ldconfig

RUN apt install tesseract-ocr -y && apt install libtesseract-dev -y

RUN cd /usr/local/share/tessdata && wget -O por.traineddata https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata?raw=true && wget -O eng.traineddata https://github.com/tesseract-ocr/tessdata/blob/main/eng.traineddata?raw=true

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "make", "run"]