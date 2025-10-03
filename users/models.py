from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re
# Create your models here.
def valiate_college_email(email):
    """ Accepts only emails that contains '.edu' or  '.ac',anywhere in email,or raises  Validation error if not
    """
    if not re.search(r'\.(edu|ac)',email):
        raise ValidationError("Please use a valid college email (.edu or .ac ) ")

class CustomUser(AbstractUser):
    #    Extends Django's AbstractUser to enforce:
    # - unique college email
    # - optional admin flag for platform management
    email=models.EmailField(unique=True,validators=[valiate_college_email])
    is_admin=models.BooleanField(default=False)
    def __str__(self):
        return self.username