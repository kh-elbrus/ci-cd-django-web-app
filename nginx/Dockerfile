FROM nginx
LABEL name="nginx"
RUN mkdir /etc/nginx/ssl
RUN chmod 700 /etc/nginx/ssl
COPY ./certs/blog.crt /etc/nginx/ssl/blog.crt
COPY ./certs/blog.key /etc/nginx/ssl/blog.key

RUN rm /etc/nginx/nginx.conf
ADD ./config/nginx.conf /etc/nginx/nginx.conf
ADD ./config/blog.conf /etc/nginx/conf.d/blog.conf
