Alexandria
==========
#### A barebone fullstack webapp of Flask (SqlAlchemy), MySQL, VueJS & NginX

3 Docker services:
 - Flask (With SQLAlchemy)
 - MySQL
 - NginX


How to run in development mode
----------
```
docker-compose up
```
Start the database and Flask backend.

```
npm install
npm run dev
```
Start a webpack dev-server with a hotreload Vuejs framework.

How to run in production mode
----------

```
docker-compose --profile production up
```
Start the production environment. The biggest difference is that the webpack dev-server is replaced with a Docker NginX service.

What is Alexandria?
----------
This repository is a collection of development/production environments. The idea is to keep everything as barebone as possible to not need too much information and setup before you see something working on the screen. 