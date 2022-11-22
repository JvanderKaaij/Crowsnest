Alexandria
==========
#### A barebone fullstack webapp of Flask (SqlAlchemy), MySQL, VueJS & NginX

3 Docker services:
 - Flask (With SQLAlchemy)
 - MySQL
 - NginX


How to run in development mode
----------

### Backend
Start the database and Flask backend.
```
docker-compose up
```
If you run this application for the first time and want to setup the database. Make sure you shell into the api container and run:


```
python setup.py
```
This will create a database structure that relates to your SQLAlchemy models and 

### Frontend

Start a webpack dev-server with a hotreload Vuejs framework.

```
npm install
npm run dev
```


How to run in production mode
----------

```
docker-compose --profile production up
```
Start the production environment. The biggest difference is that the webpack dev-server is replaced with a Docker NginX service.

What is Alexandria?
----------
This repository is a collection of development/production environments. The idea is to keep everything as barebone as possible to not need too much information and setup before you see something working on the screen. 