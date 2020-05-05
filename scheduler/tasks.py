from celery import Celery

app = Celery('tasks', broker='pyamqp://claw:test@localhost/myvhost', backend="rpc://claw@test@localhost/myvhost")

@app.task
def add(x, y):
    return x + y
    
