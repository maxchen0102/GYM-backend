from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # 使用django內建方法註冊登入
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'login.html')


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

        return render(request, 'login.html',{'form': form})



@csrf_exempt
def enroll(request):
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
            return JsonResponse({"status": "error"})
    else:

        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'enroll.html', context)


# 使用django內建方法註冊登入
@csrf_exempt
def enroll2(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user=User.objects.create_user(username=username, password=password)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


def test(request):
    return render(request, 'test.html')


@csrf_exempt
def certificate(request):
    cn = request.POST.get('cn')
    san = request.POST.get('san')
    data = {
        "cn": cn,
        "san": san
    }
    return JsonResponse({"status": "success", "data": data})

