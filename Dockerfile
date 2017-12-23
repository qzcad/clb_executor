FROM python:3.5
ADD requirements.txt /app/requirements.txt
ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A executor worker --concurrency=20 --loglevel=info