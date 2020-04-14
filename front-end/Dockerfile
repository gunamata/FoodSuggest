FROM node:12.10

RUN mkdir -p /usr/src/front-end

WORKDIR /usr/src/front-end

COPY package*.json ./

RUN npm install

COPY . .