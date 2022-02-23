FROM python:3.8-slim-buster
RUN mkdir code
WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN apt-get update && pip install -U -r ./requirements.txt

#COPY ./entrypoint.sh ./entrypoint.sh
#RUN ls
#RUN chmod +x entrypoint.sh

ENTRYPOINT ./entrypoint.sh