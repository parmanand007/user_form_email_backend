from django.urls import path
from .views import UserFormAPIView, UserFormListAPIView

urlpatterns = [
    path('api/user-form', UserFormAPIView.as_view(), name='user_form_api'),
    path('api/user-form/all', UserFormListAPIView.as_view(), name='user_list_api'),  # New URL pattern
    # Add other URL patterns as needed
]
