'''This example is provided with no gurantee that it will work right out of the box for you. It merely provides a starting point
for those flailing to get their celery app working properly. We have highlight what will require changes from your end. 
There are probably more efficient ways to go about what we needed to achieve...but this has worked for us and has been 
extremely stable. '''


import os, time, config
from celery import Celery

dburl= os.environ.get('POSTGRES_URL')   #
engine = sa.create_engine(dburl)

app = Celery('tasks')
app.config_from_object(config)    #this configures your celery app. Take a look at the config.py file

app.config_from_object(config)

@app.task
def task1():
    '''This is an example of a task that will be run as a result of being called from another module. 
      For example, in our case, we need to check whether any files have been dropped into a certain folder in 
      Google Drive. So, let's say we have a script called check_drive. Once check_drive has done it's thing
      the last line of code is: task1.delay(). That calls this task.'''
    import some_task1   #what script do you want to run? as per the long winded note above, it would be check_drive
    task_wait_time = 60   #how long do you want to wait until you run it? This time is in seconds
    print ('Will read emails again in ' + str(int(task_wait_time)) + ' seconds')
    time.sleep(reader_wait)
    print ("Running module: some_task1")
    some_task1()
    del reader_wait   #the next 3 lines help with memory leaks. It is a problem we faced on Heroku
    import gc
    gc.collect()

@app.task
def some_task2():
    '''This is an example of using celery_beat to schedule the tasks. This better for discrete tasks that don't 
    run to frequently. To run tasks like this, you need to configure the beat schedule. While at first, it seems
    easier to do in this module, it's a lot cleaner to do it in a config file.''' 
    import some_task2
    some_task2()
    del scraper_wait
    import gc
    gc.collect()

