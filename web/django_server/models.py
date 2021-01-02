from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Member(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=14, null=True)
    email = models.EmailField(max_length=255, blank=True)
    password = models.CharField(max_length=50, null=True)
    birth = models.DateField()
    sex = models.CharField(max_length=1)
    tags = ArrayField(models.CharField(max_length=200), null=True)
    is_active = models.BooleanField(default=False)
    last_signin = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.user.email} {self.name} {self.phone}, {self.tags}'
