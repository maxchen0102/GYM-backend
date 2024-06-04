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


@csrf_exempt
def deleteCategory(request):
    id = request.POST.get('id')
    category = Category.objects.get(id=id)
    category.delete()
    return JsonResponse({"status": "success"})

@csrf_exempt
def updateCategory(request):
    id = request.POST.get('id')
    name = request.POST.get('name') # new name
    category = Category.objects.get(id=id) # get the category
    category.name = name
    category.save()
    return JsonResponse({"status": "success"})




@csrf_exempt
def add_item(request):
    name = request.POST.get('name')
    category_id = request.POST.get('category_id')
    category = Category.objects.get(id=category_id)
    item = Item(name=name, category=category)
    item.save()
    return JsonResponse({"status": "success"})

@csrf_exempt
def get_items(request):
    category_id = request.POST.get('category_id')
    items = Item.objects.filter(category=category_id)
    items = [item.name for item in items] # get the names of the items
    return JsonResponse({"status":"success","items": items})