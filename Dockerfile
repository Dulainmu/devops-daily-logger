FROM python:3.9-slim

WORKDIR /app

COPY log.py .

RUN mkdir -p /app/logs

CMD ["python", "log.py"]
