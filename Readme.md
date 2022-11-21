Alexandria
==========
#### A barebone fullstack webapp of: Flask (SqlAlchemy), MySQL, VueJS, NginX

There are 3 Docker services.
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
Start the production environment. The biggest difference is that the webpack dev-server is replaced with a docker NginX service.