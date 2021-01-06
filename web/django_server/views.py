from django.contrib.auth.models import User
from django.contrib import auth
import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django_server.models import Member
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=user_email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': '이메일이나 비번이 정확하지 않습니다.'})
    return render(request, 'login.html')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {})
    else:
        user = Member.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            password = request.POST.get('password'),
            birth = request.POST.get('birth'),
            sex = request.POST.get('sex'),
            phone = request.POST.get('phone')    
        )
        return redirect('index')

@login_required
@require_http_methods(['GET', 'POST'])
def modify(request, pk):
    if request.method == 'GET':
        return render(request, 'modify.html', {'user': user})
    else:
        user = Member.objects.update(
            email = request.POST.get('email'),
            password = request.POST.get('password'),
            birth = request.POST.get('birth'),
            sex = request.POST.get('sex'),
            phone = request.POST.get('phone')    
        )
        return redirect('index')

@require_http_methods(['GET'])
def index(request):
    member_list = Member.objects.all().order_by('name')
    search_name = request.GET.get('search_name')
    if search_name:
        member_list = member_list.filter(name__icontains=search_name)

    return render(request, 'index.html', {'member_list': member_list})


@require_http_methods(['GET'])
def detail_info(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'detail.html', {'member': member})
    