import os 
from celery import Celery 

# set the default Django settings module for the 'celery' program. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignments.settings') 

app = Celery('assignments') 

app.config_from_object('django.conf:settings', 
					namespace='CELERY') 

# Load task modules from all registered Django app configs. 
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}') 
