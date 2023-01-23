Crowsnest
==========
#### A Hardware & Student Library Tool

3 Docker services:
 - Flask (With SQLAlchemy)
 - MySQL
 - NginX


How to run in development mode
----------

### Backend

Create a folder /config and add a file in there called config.env
In that config file make sure the following settings are present:

Start the database and Flask backend.
```
docker-compose --env-file config/config.env up
```
If you run this application for the first time and want to setup the database. Make sure you shell into the api container and run:


```
python setup.py
```
This will create a database structure that relates to your SQLAlchemy models and 

#### Authentication
It's important to mention that nothing of this project is safe to use in production without changing.
- The MySQL root password in docker-compose should be changed.
- The setup.py username and password should be changed.
- The secret key in the runtime module should be changed.

### Frontend

Start a webpack dev-server with a hotreload Vuejs framework.

```
npm install
npm run dev
```


How to run in production mode
----------
### Backend

Create a folder /config and add a file in there called config.env
In that config file make sure the following settings are present:
```
SQL_ROOT_PASS={password}
COOKIE_SECRET={secret}
```

```
docker-compose --env-file config/config.env up
```

### New Crowsnest Admin User

Login to the the api container
```
docker exec -it [container_name] /bin/sh
```

Run the python script to add a new user:
```
python user_setup.py {username} {password} {user_type}
```

Note that the user_type may already exist - or is created new when it doesn't

### Frontend

I use the local Apache server to serve the frontend files. You can build it with the dev commands and point the Apache server to the /dist folder.

```
npm run dev
```