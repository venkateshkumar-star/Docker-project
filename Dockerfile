FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask

ARG APP_VERSION=v1.0.0
ENV APP_VERSION=${APP_VERSION}

EXPOSE 5000

CMD ["python", "app.py"]
