FROM python:3.11-slim

WORKDIR /main
#/app



COPY  requirements.txt /main

RUN python -m venv /opt/venv
ENV PATH="opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


ENV PYTHONUNBUFFERED 1

COPY . /app


CMD ["python", "main.py", "runserver", "0.0.0.0:80"]