from __future__ import absolute_import

import os
from celery import Celery

broker_host = os.environ['BROKER_HOST']
broker_port = os.environ['BROKER_PORT']
broker_user = os.environ['BROKER_USER']
broker_pass = os.environ['BROKER_PASS']

app = Celery('executor',
             broker='amqp://{}:{}@{}:{}'.format(broker_user, broker_pass,
                                                broker_host, broker_port),
             backend='rpc://')
