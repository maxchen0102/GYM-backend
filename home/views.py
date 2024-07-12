from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # 使用django內建方法註冊登入
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from utils import is_admin
from django.contrib.auth import logout
import json

# Create your views here.
# Create your views here.


def home(request):
    return redirect('sign_in')


def sign_out(request):
    logout(request)
    return redirect('sign_in')

@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('introduce_page')
        else:
            return JsonResponse({"status": "error"})
    else:
        form = AuthenticationForm()

        return render(request, 'login.html', {'form': form})


@csrf_exempt
def sign_up(request):
    # data = json.loads(request.body)
    # username = data.get('username')
    # password1 = data.get('password1')
    # password2 = data.get('password2')
    print(request.POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(username, raw_password)
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('introduce_page')
        else:
            print(form.errors)  # 印出錯誤訊息
            return JsonResponse({"status": "error"})
    else:

        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'enroll.html', context)


@login_required
def introduce_page(request):
    return render(request, 'introduce_page.html')


@csrf_exempt
def enroll2(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


@user_passes_test(is_admin, login_url='/permission_denied/')
@login_required
def detail(request):
    return render(request, 'detail.html')


@csrf_exempt
def certificate(request):
    cn = request.POST.get('cn')
    san = request.POST.get('san')
    data = {
        "cn": cn,
        "san": san
    }
    return JsonResponse({"status": "success", "data": data})
