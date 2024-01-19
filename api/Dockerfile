FROM python:3.7-alpine
WORKDIR /usr/src/app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV FLASK_APP=runtime.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=true

# apk is the package manager for alpine images
# mariadb-connector is needed for installing the mysqlclient pip package
RUN apk add --no-cache gcc musl-dev linux-headers mariadb-connector-c-dev

# I still don't fully undertand why requirements.txt needs to be copied seperatly
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run"]