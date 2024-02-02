

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User
from django.conf import settings

@receiver(post_save, sender=User)
def send_form_submission_email(sender, instance, created, **kwargs):
    """
    Signal receiver function to send an email when a user object is saved.
    """
    if created:  # Only send email for newly created user objects
        try:
            send_mail(
                'Form Submission Confirmation',
                'Thank you for submitting the form!',
                settings.SENDER_EMAIL, [instance.email],
                fail_silently=False,
            )
        except Exception as e:
            pass  # Handle email sending failure if needed
