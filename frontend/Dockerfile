FROM node:14.17.3

COPY . /app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN yarn install

# 앱 실행
CMD ["yarn", "start"]