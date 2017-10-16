FROM python:2.7.13-stretch

MAINTAINER Shawn M. Jones <jones.shawn.m@gmail.com>

RUN apt-get update -y 

# install Java for Java stuff
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y default-jdk
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libgmp3-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libxml2-dev libxmlsec1-dev

# clean apt cache
RUN DEBIAN_FRONTEND=noninteractive apt-get clean

# copy over application stuff
COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt --no-cache-dir
