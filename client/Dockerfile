FROM node:18-alpine as react-build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . ./

RUN npm run build

FROM nginx:stable-alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf /etc/nginx/conf.d

COPY conf/default.conf /etc/nginx/conf.d/default.conf

COPY --from=react-build /app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]