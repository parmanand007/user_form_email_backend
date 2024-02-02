import os 
from celery import Celery 
from django.conf import settings


# set the default Django settings module for the 'celery' program. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignments.settings') 

# app = Celery('assignments') 
app = Celery('assignments',
             backend='redis://default:4B5jgDE2hFOfoPpPDOeJBfic2ANComeo@roundhouse.proxy.rlwy.net:46494',
             broker='redis://default:4B5jgDE2hFOfoPpPDOeJBfic2ANComeo@roundhouse.proxy.rlwy.net:46494'
             )

# Using a string here means the worker doesn't 
# have to serialize the configuration object to 
# child processes. - namespace='CELERY' means all 
# celery-related configuration keys should 
# have a `CELERY_` prefix. 
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY') 

# Load task modules from all registered Django app configs. 
app.autodiscover_tasks() 

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
