from django.contrib.auth.models import User
from django.contrib.auth import login as al, authenticate
import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django_server.models import Member
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        if user and user.password == password:
            al(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 정확하지 않습니다.'})


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {})
    else:
        user = User.objects.create(username=request.POST.get('email'), password=request.POST.get('password'), email=request.POST.get('email'))
        member = Member.objects.create(
            user = user,
            name = request.POST.get('name'),
            birth = request.POST.get('birth'),
            sex = request.POST.get('sex'),
            phone = request.POST.get('phone')    
        )
        
        return redirect('index')

@login_required
@require_http_methods(['GET', 'POST'])
def modify(request, pk):
    user = request.user
    member = Member.objects.get(user=user)
    if request.method == 'GET':
        return render(request, 'modify.html', {'pk':pk, 'member':member})
    else:
        birth = request.POST.get('birth')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        
        if birth:
            member = Member.objects.update(birth=birth)
        if sex:
            member = Member.objects.update(sex=sex)
        if phone:
            member = Member.objects.update(phone=phone)
        
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
    