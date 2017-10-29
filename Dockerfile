FROM alpine:3.6
RUN apk update
RUN apk add --no-cache python3 py-psycopg2 &&\
    pip3 install chaperone
ADD requirements.txt /
RUN pip3 install -r /requirements.txt
ADD . /app/
RUN mkdir /etc/chaperone.d
COPY chaperone.conf /etc/chaperone.d/chaperone.conf
EXPOSE 5000
ENTRYPOINT ["/usr/bin/chaperone"]
