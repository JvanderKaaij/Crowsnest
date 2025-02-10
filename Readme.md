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

Start the full service for development:

```
docker-compose -f docker-compose.dev.yaml build
docker-compose -f docker-compose.dev.yaml up
```

If you run this application for the first time and want to setup the database. Make sure you shell into the api container and run:

```
docker exec -it crowsnest-api sh
python dev_data_setup.py
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


Create a file named secret.env in the root of the project.
In that config file make sure the following settings are present:
```
COOKIE_SECRET={secret}
MYSQL_ROOT_PASSWORD={password}
MYSQL_USER={username}
MYSQL_PASSWORD={password}
MYSQL_DATABASE={db}
MJ_APIKEY_PUBLIC={public_key}
MJ_APIKEY_PRIVATE={private_key}
```

run on live:

```
docker-compose -f docker-compose.live.yaml up
```

### New Crowsnest Admin User

Login to the the api container
```
docker exec -it [container_name] /bin/sh
```

Run the python script to add a new user:
```
python user_setup.py {string:username} {string:password} {string:user_type}
```

Note that the user_type may already exist - or is created new when it doesn't

### Frontend

served files are in /dist folder

to rebuild (during development for instance):

```
npm run dev
```

If refreshing the page gives a 404?
Make sure the .htaccess file is present in the /dist folder!

### MailJet

TODO:
Cron job for 