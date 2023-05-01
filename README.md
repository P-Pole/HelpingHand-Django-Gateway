# HelpingHand-Django-Gateway
Django API Gateway for Helping Hand Web App
----
This is a Django Gateway part of a microservices based architecture application that consists of:

React/HTML/CSS front end - https://github.com/P-Pole/HelpingHand-v2

Dockerized Django DB/Server - https://github.com/P-Pole/HelpingHand-Django-Server

Dockerized Flask DB/Server - https://github.com/P-Pole/HelpingHand-Flask-Docker-Server

Django Gateway connecting front-end with back-end - https://github.com/P-Pole/HelpingHand-Django-Gateway


---
How to deploy application:

1. Start with Dockerized Django Server.
2. Use "docker-compose up db" from the main directory of a project to build database.
3. Once it is up and running use "docker-compose up web" to run a server.
4. Do the same for Flask Db/Server using "docker-compose up db" and "docker-compose up backend"
5. Start gateway server by using "python manage.py runserver"
6. In React app use "npm run dev"

Application will be up and running.
