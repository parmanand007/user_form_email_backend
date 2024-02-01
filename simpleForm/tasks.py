# tasks.py

from celery import shared_task



from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_form_submission_email(user_email):
    email_subject = 'Thank you for your submission'
    email_message = 'Thank you for submitting the form!'
    send_mail(email_subject, email_message, settings.SENDER_EMAIL, ['parmanandprajapati006@gmail.com'])
    return

