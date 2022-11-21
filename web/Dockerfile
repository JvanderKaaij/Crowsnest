FROM nginx:alpine as production
WORKDIR /usr/share/nginx/html

RUN apk add --update nodejs npm

COPY package*.json ./
COPY webpack.config.js webpack.config.js

COPY . .

EXPOSE 80