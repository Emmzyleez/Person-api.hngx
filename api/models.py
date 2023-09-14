from django.db import models
from django.core.validators import RegexValidator

string_only_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]*$',
    message='Only strings are allowed.',
    code='invalid_string'
)


class Person(models.Model):
    name = models.CharField(max_length=250, validators=[string_only_validator])

# Create your models here.
