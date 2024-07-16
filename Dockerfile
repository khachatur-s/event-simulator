FROM python:latest
LABEL org.opencontainers.image.source="https://github.com/khachatur-s/event-simulator"
LABEL org.opencontainers.image.description="Event Log Simulator"
LABEL org.opencontainers.image.licenses=Unlicense
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY event-simulator.py ./

CMD [ "python", "./event-simulator.py" ]
