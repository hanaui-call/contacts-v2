import logging

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

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
    return render(request, 'index.html', {})
