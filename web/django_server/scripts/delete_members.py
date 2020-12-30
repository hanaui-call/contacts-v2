from django_server.models import Member
from django.contrib.auth.models import User


def run(*args):
    Member.objects.all().delete()
    User.objects.all().delete()

    print('All members are deleted.')
