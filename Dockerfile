FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ARG APP_VERSION=V1.00
ENV APP_VERSION=$APP_VERSION

CMD ["python", "app.py"]
