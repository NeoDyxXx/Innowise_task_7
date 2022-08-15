FROM python:3.8-slim-buster

RUN pip install pandas

RUN mkdir app
WORKDIR ./app
RUN mkdir logs

COPY . .

ENV DIRECTORY_OF_LOGS='/app/logs'

CMD [ "python", "simulator.py"]