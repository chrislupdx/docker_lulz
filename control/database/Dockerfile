FROM postgres:14.3
RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias de_DE.UTF-8
ENV LANG de_DE.utf8


# FROM ubuntu:latest
# FROM library/postgres
# COPY init.sql /docker-entrypoint-initdb.d/init.sql
# MAINTAINER chrisl chlu@pdx.edu

# RUN apt-get -y update
# RUN apt-get -y upgrade
# RUN apt-get install -y build-essential

# ENV POSTGRES_PASSWORD=secret
# ENV POSTGRES_USER=username
# ENV POSTGRES_DB=database
# COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
