FROM python:3.10.12

ENV PYTHONUNBUFFERED 1 

RUN apt-get -y update 
RUN apt-get -y install vim 

RUN mkdir /srv/backend
ADD . /srv/backend

WORKDIR /srv/backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

-----------------------------------------

FROM python:3.10.12

ENV PYTHONUNBUFFERED 1 

RUN apt-get -y update 
RUN apt-get -y install vim 

RUN mkdir /srv/backend
ADD . /srv/backend

WORKDIR /srv/backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py migrate