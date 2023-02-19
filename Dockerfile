FROM python:3.9.16-alpine3.17

RUN mkdir /home/data /home/output

ADD script.py /home

WORKDIR /home

CMD [ "python3", "script.py" ]