FROM mysql

# run create.sql on init
# on later starts, create.sql will not be run again
ADD create.sql /docker-entrypoint-initdb.d

EXPOSE 3306