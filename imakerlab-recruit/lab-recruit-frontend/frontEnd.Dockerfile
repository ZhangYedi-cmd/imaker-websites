FROM node:14-alpine as builder

WORKDIR /code

# 先将依赖目录转入到code目录 -- 判断这一层的文件是否和缓存相同
ADD package.json yarn.lock /code/
# 如果相同， yarn就不会执行
RUN yarn install

# 再将src下更新的代码cope到code目录下
ADD . /code

RUN yarn build # 打包

FROM nginx:alpine

ADD nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder ./code/dist /usr/share/nginx/html
