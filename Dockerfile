FROM python:3.10.12

ENV PYTHONUNBUFFERED 1 

RUN apt-get -y update 
RUN apt-get -y install vim 

RUN mkdir /mealbuddy/mealbuddy_backend
ADD . /mealbuddy/mealbuddy_backend

WORKDIR /mealbuddy/mealbuddy_backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
