"""
Convenience executable to start celery worker across the cluster.
"""
from fabric import ThreadingGroup
import argparse

# not working with authentication

def main(hosts, concurrency):
    with ThreadingGroup(*hosts) as sg:
        results = sg.run('/home/claw/anaconda3/bin/activate py36 && '
                         f'celery multi start w1 -A scheduler '
                         f'--concurrency={concurrency} '
                         f'-l info -n %h --pidfile=/var/run/celery/%n.pid --logfile=/var/log/celery/%n%I.log')
                         
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Start celery worker')
    parser.add_argument('--concurrency', type=int, default=20, help='worker concurrency')
    args = parser.parse_args()
    main(['localhost'], args.concurrency)
