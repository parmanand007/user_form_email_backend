from django.urls import path
from .views import UserFormAPIView, UserFormListAPIView, RunCelery

urlpatterns = [
    path('api/celery', RunCelery.as_view(), name='celery'),
    path('api/user-form', UserFormAPIView.as_view(), name='user_form_api'),
    path('api/user-form/all', UserFormListAPIView.as_view(), name='user_list_api'),  # New URL pattern
    # Add other URL patterns as needed
]
