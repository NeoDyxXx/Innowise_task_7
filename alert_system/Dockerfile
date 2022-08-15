FROM python:3.8-slim-buster

RUN pip install pandas
RUN pip install watchdog

RUN mkdir app
WORKDIR ./app
RUN mkdir logs

COPY . .

ENV DEFAULT_DIR='./logs'

CMD [ "python", "monitor_directory.py"]