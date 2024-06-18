from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User


# Create your views here.

def home(request):
    return render(request, 'login.html')


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # user = User.objects.filter(username=username, password=password)
    # if user.exists():
    #     return JsonResponse({"status": "success"})
    # else:
    #     return JsonResponse({"status": "error"})
    return JsonResponse({"status": "success" , "username": username, "password": password})

@csrf_exempt
def enroll(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    user = User(username=username, password=password, phone=phone, email=email)
    user.save()
    return JsonResponse({"status": "success"})


# 使用django內建方法註冊登入
@csrf_exempt
def enroll2(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user=User.objects.create_user(username=username, password=password)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})

