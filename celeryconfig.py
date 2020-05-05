broker_url = 'pyamqp://claw:test@localhost/myvhost'
result_backend = 'rpc://claw@test@localhost/myvhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'US/Pacific'
enable_utc = True
