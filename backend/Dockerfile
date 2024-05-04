FROM python:3.12.1-slim-bullseye


WORKDIR /app

ADD pyproject.toml /app/

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

RUN pip install --upgrade pip
RUN pip install poetry


RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/