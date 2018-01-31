from __future__ import absolute_import

import os

from celery import Celery
from cluster_tasks import __tasks__

broker_host = os.environ['BROKER_HOST']
broker_port = os.environ['BROKER_PORT']
db_number = os.environ['DB_NUMBER']

broker_url = 'redis://{host}:{port}/{db_number}'.format(
    host=broker_host,
    port=broker_port,
    db_number=db_number
)

app = Celery('executor', broker=broker_url)

app.conf.result_backend = broker_url

for task in __tasks__:
    app.task(task)
