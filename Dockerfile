FROM python:3.5.0

MAINTAINER Leandro Silva

RUN apt-get update
RUN apt-get install -y git
RUN useradd wttd -m
RUN mkdir /wttd
WORKDIR /wttd
RUN git clone https://github.com/ldfsilva/eventex.git .
COPY contrib/env-sample .env
RUN pip install -r requirements.txt

RUN chown -R wttd /wttd
USER wttd

EXPOSE 8000

ENTRYPOINT ["/wttd/contrib/django_start.sh"]
