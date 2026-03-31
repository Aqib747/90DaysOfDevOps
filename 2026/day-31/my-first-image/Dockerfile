#take the base image as ubuntu

FROM ubuntu

#who built this 

LABEL maintainer="aqib"

#set working directory

WORKDIR /app

#install curl

RUN apt-get update && apt-get install -y curl

CMD ["echo", "hello form mu custom image"]
