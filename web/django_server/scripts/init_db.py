from django_server.models import Member
from django.contrib.auth.models import User
from django_server.const import SexEnum

import datetime


def run(*args):
    members = [
        {
            'name': '홍길동',
            'email': 'kdhong@hanaui.net',
            'password': '12345',
            'birth': datetime.date(1997, 10, 19),
            'sex': SexEnum.MALE.value,
            'phone': '010-1234-5678',
            'tags': ['가족모임리더', '소명센터'],
        },
        {
            'name': '김영희',
            'email': 'yhkim@hanui.net',
            'password': '09876',
            'birth': datetime.date(1982, 2, 3),
            'sex': SexEnum.FEMALE.value,
            'phone': '010-6789-1234',
            'tags': [],
        }
    ]

    for m in members:
        user = User.objects.create(username=m['email'], password=m['password'], email=m['email'])

        member = Member.objects.create(
            user=user,
            name=m['name'],
            phone=m['phone'],
            birth=m['birth'],
            sex=m['sex'],
            tags=m['tags'],
            is_active=True,
        )
        print(member)
