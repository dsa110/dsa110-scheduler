from .celery import app
import scipy
import casatools

# demo tasks
@app.task
def add(x, y):
    return x + y
    
@app.task
def close():
    sim = casatools.simulator()
    return sim.close()
