FROM python:3.8
MAINTAINER Dreipoe & Co.

ENV PYTHONUNBUFFERED 1

RUN apt update || apt upgrade

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser --disabled-password --gecos '' python
RUN adduser python sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER python
