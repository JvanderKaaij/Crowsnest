FROM python:3.7-alpine
WORKDIR /usr/src/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV FLASK_APP=runtime.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=true
ENV MJ_APIKEY_PUBLIC=46b7fb7a382ca67515e32250e3b49e5a
ENV MJ_APIKEY_PRIVATE=0b744c249c8c1b4efa02cda15bc1555e

# apk is the package manager for alpine images
# mariadb-connector is needed for installing the mysqlclient pip package
RUN apk add --no-cache gcc musl-dev linux-headers mariadb-connector-c-dev

# I still don't fully undertand why requirements.txt needs to be copied seperatly
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run"]