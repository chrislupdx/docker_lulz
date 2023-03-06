FROM ubuntu:latest
FROM library/postgres
COPY init.sql /docker-entrypoint-initdb.d/
MAINTAINER chrisl chlu@pdx.edu
 
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential
