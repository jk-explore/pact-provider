# Set the base image
FROM ubuntu
USER root
RUN apt-get update
RUN apt-get -y install python-dev
RUN apt-get -y install python-pip
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-rest-swagger
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
