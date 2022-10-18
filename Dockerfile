FROM python:3

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt