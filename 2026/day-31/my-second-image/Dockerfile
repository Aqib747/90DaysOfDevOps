FROM ubuntu


WORKDIR /app



RUN apt-get update && \ 
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*	


COPY app.sh .

RUN chmod +x app.sh

EXPOSE 8080

CMD ["./app.sh"]

