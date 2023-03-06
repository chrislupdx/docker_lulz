FROM ubuntu:latest
FROM library/postgres
COPY init.sql /docker-entrypoint-initdb.d/init.sql
MAINTAINER chrisl chlu@pdx.edu
 
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential

# ENV POSTGRES_PASSWORD=secret
# ENV POSTGRES_USER=username
# ENV POSTGRES_DB=database
# COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
