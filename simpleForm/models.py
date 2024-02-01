# In user_form/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.validators import validate_international_phonenumber


class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, phone_number, password=None,**kwargs):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, phone_number, password,**kwargs):
        user = self.create_user(
            email,
            date_of_birth,
            phone_number,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
def validate_age(date_of_birth):
    if (timezone.now().date() - date_of_birth).days < 18 * 365.25:
        raise ValidationError("Must be at least 18 years old to register")

class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_international_phonenumber]


class User(AbstractBaseUser):
    name=models.CharField(max_length=100,default='')
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(validators=[validate_age])
    phone_number =PossiblePhoneNumberField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'phone_number']
    
    class Meta:
        unique_together = ('email', 'phone_number')
        db_table = "form_user"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
