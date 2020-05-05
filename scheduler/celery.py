from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('scheduler',
             broker='pyamqp://claw:test@localhost/myvhost',
             backend='rpc://claw@test@localhost/myvhost',
             include=['scheduler.tasks'])

app.conf.update(result_expires=3600)

if __name__ == '__main__':
    app.start()
    
