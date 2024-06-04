from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Item, List
# Create your views here.

def personPage(request):
    return JsonResponse({"status": "success"})

@csrf_exempt
def getPersonalCategory(request):
    UUID = request.POST.get('UUID')
    categories = Category.objects.filter(UUID=UUID)
    category_names = [category.name for category in categories]
    return JsonResponse({"status":"success","category_names": category_names})

@csrf_exempt
def addCategory(request):
    name = request.POST.get('name')
    UUID = request.POST.get('UUID')
    category = Category(name=name,UUID=UUID)
    category.save()
    return JsonResponse({"status": "success"})
