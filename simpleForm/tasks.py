# tasks.py
from celery import Celery, shared_task



from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_form_submission_email(user_email):
    print("===================>send_form_submission")
    email_subject = 'Thank you for your submission'
    email_message = 'Thank you for submitting the form!'
    try:
        send_mail(email_subject, email_message, settings.SENDER_EMAIL, [user_email])
    except Exception as e:
        print("exception is",e)
    return

@shared_task
# @app.task(bind=True)
def add_num(args):
    print(f"--------  {args}")