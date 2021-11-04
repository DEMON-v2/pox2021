FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y
RUN apt install curl -y
RUN apt install apache2 php -y
RUN apt install libapache2-mod-php -y

COPY ./apache2.conf /etc/apache2/apache2.conf
COPY ./flag /

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data

EXPOSE 3192

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]