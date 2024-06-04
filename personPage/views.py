from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Item, List
# Create your views here.

def personPage(request):
    return JsonResponse({"status": "success"})

def getPersonalCategory(request):
    id = request.GET.get('id')
    category = Category.objects.get(id=id)
