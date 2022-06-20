FROM python:latest
LABEL org.opencontainers.image.source="https://github.com/khachatur-s/event-simulator"
ENV PYTHONUNBUFFERED=0
WORKDIR /usr/src/app

COPY event-simulator.py ./

CMD [ "python", "./event-simulator.py" ]
