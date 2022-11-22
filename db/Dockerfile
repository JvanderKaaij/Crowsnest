FROM mysql:5.7

EXPOSE 3306

# run create.sql on init
# on later starts, create.sql will not be run again
ADD create.sql /docker-entrypoint-initdb.d