FROM python:2.7.13-stretch

MAINTAINER Shawn M. Jones <jones.shawn.m@gmail.com>

RUN apt-get update -y 

# install Java for Java stuff
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y default-jdk
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git

# clean apt cache
RUN DEBIAN_FRONTEND=noninteractive apt-get clean

COPY requirements.txt /app
WORKDIR /app
RUN pip install -r /app/requirements.txt --no-cache-dir

# copy over application stuff
COPY . /app

# set up environment
WORKDIR /app
