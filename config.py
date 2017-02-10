import os

timezone = 'America/Los_Angeles'    #It is important to set a timezone if you want celery beat to work
broker_url = os.environ.get('REDIS_URL')    
result_backend = os.environ.get('REDIS_URL')
broker_pool_limit = None

'''As per the tasks created in the celery_app example module, only task2 is running on celery_beat. So, we will
  only include that in the beat schedule below. The schedule times are in seconds. '''

beat_schedule = {
                'task2: {
                    'task': 'task2',
                    'schedule': 3600
                                },               
                }


