# dsa110-scheduler
Task scheduler in celery (Issues at https://github.com/dsa110/dsa110-issues)


## Setup

1. Start [rabbitmq](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#rabbitmq). "myvhost", "claw"
2. Start [celery](https://docs.celeryproject.org/en/stable/getting-started/brokers/rabbitmq.html#starting-stopping-the-rabbitmq-server):
  `celery -A scheduler worker --loglevel=INFO`
3. Start IPython
4. Submit task, e.g.,
```
In [1]: from scheduler import tasks                                                                                                            
In [2]: res = tasks.add.delay(4,4)                                                                                                             
In [3]: res.get()                                                                                                                              
Out[3]: 8
```

5. Celery server will log as follows:
```
[2020-10-23 15:40:34,236: INFO/MainProcess] Connected to amqp://claw:**@127.0.0.1:5672/myvhost
[2020-10-23 15:40:34,295: INFO/MainProcess] mingle: searching for neighbors
[2020-10-23 15:40:35,325: INFO/MainProcess] mingle: all alone
[2020-10-23 15:40:35,461: INFO/MainProcess] celery@dsahead ready.
[2020-10-23 15:44:41,365: INFO/MainProcess] Received task: scheduler.tasks.add[8b14a736-fa90-4161-b120-f315c4558ae0]  
[2020-10-23 15:44:41,392: INFO/ForkPoolWorker-31] Task scheduler.tasks.add[8b14a736-fa90-4161-b120-f315c4558ae0] succeeded in 0.01884270552545786s: 8
```
