import logging

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django_server.models import Member
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@require_http_methods(['POST'])
def signup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    birth = request.POST.get('birth')
    sex = request.POST.get('sex')
    phone = request.POST.get('phone')

    return redirect('index')


@require_http_methods(['POST'])
def modify(request):
    pass

@require_http_methods(['GET'])
def index(request):
    member_list = Member.objects.all().order_by('name')
    search_name = request.GET.get('search_name')
    if search_name:
        member_list = member_list.filter(name__icontains=search_name)

    return render(request, 'index.html', {'member_list': member_list})
