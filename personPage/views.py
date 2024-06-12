from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Category, Item, List
from utils import hello_decorator

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status


# Create your views here.
#hello world 

def personPage(request):
    return JsonResponse({"status": "success"})


# 取得分類
@csrf_exempt
def getPersonalCategory(request):
    UUID = request.POST.get('UUID') # get the UUID
    categories = Category.objects.filter(UUID=UUID)
    category_names = [category.name for category in categories]
    return JsonResponse({"status":"success","category_names": category_names})

# 新增分類
@csrf_exempt
def addCategory(request):
    name = request.POST.get('name')
    UUID = request.POST.get('UUID')
    category = Category(name=name,UUID=UUID)
    category.save()
    return JsonResponse({"status": "success"})


# 刪除分類
@csrf_exempt
def deleteCategory(request):
    id = request.POST.get('id')
    category = Category.objects.get(id=id)
    category.delete()
    return JsonResponse({"status": "success"})

# 更新分類
@csrf_exempt
def updateCategory(request):
    category_id = request.POST.get('category_id')     # category id
    category_new_name = request.POST.get('category_new_name')  # new name
    category = Category.objects.get(id=category_id)  # get the category
    category.name = category_new_name
    category.save()
    return JsonResponse({"status": "success"})




# 新增此分類之健身項目
@csrf_exempt
def add_item(request):
    name = request.POST.get('name')
    category_id = request.POST.get('category_id')  # 取得category_id外鍵
    category = Category.objects.get(id=category_id)
    item = Item(name=name, category=category)
    item.save()
    return JsonResponse({"status": "success"})


# 取得此分類之健身項目
@csrf_exempt
def get_items(request):
    category_id = request.POST.get('category_id') # 用分類id取得所有屬於此分類的健身項目
    items = Item.objects.filter(category=category_id)
    items = [item.name for item in items] # get the names of the items
    return JsonResponse({"status":"success","items": items})


# 刪除此分類之健身項目
@csrf_exempt
def delete_item(request):
    item_id = request.POST.get('item_id')  # 取得此item的id
    item = Item.objects.get(id=item_id)
    item.delete()
    return JsonResponse({"status": "success"})

# 更新此分類之健身項目
@csrf_exempt
def update_item(request):
    item_id = request.POST.get('item_id')
    name = request.POST.get('name')
    item = Item.objects.get(id=item_id)
    item.name = name
    item.save()
    return JsonResponse({"status": "success"})

@csrf_exempt
def get_record_list(request):
    try:
        item_id = request.POST.get('item_id')
        items = List.objects.filter(item_id=item_id)
        items = [item.name for item in items]
        return JsonResponse({"status": "success","items": items})
    except List.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Record not found."}, status=404)
    except Exception as e:
        return JsonResponse({"status": "無法預期錯誤", "message": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def add_record_list(request):
    name = request.POST.get('name')
    item_id = request.POST.get('item_id')
    item = Item.objects.get(id=item_id)
    record = List(name=name, item=item)
    record.save()
    return JsonResponse({"status": "success"})

# @csrf_exempt
# @require_http_methods(["DELETE"])
# def delete_record_list(request):
#     try :
#         data = json.loads(request.body)
#         record_id = data['record_id']
#         record = List.objects.get(id=record_id)
#         record.delete()
#         return JsonResponse({"status": "xxxx", "message": "xxxxx"})
#     except List.DoesNotExist:
#         return JsonResponse({"status": "xxxx", "message": "xxxxx"}, status=404)
@csrf_exempt
@api_view(['DELETE'])
def delete_record_list(request):
    try:
        data = json.loads(request.body)
        record_id = data['record_id']
        record = List.objects.get(id=record_id)
        record.delete()
        return Response({"status": "success", "message": "Record deleted successfully."}, status=status.HTTP_200_OK)
    except json.JSONDecodeError:
        raise APIException("Invalid JSON format.")
    except KeyError:
        raise APIException("Record ID not provided.")
    except List.DoesNotExist:
        raise APIException("Record not found.", status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise APIException(str(e))
@csrf_exempt
@require_http_methods(["PUT"])
def update_record_list(request):
    try :
        data=json.loads(request.body)
        record_id = data['record_id']
        name=data.get('name')

        if not record_id or not name :
            return JsonResponse({"status": "fail"})
        record = List.objects.get(id=record_id)
        record.name = name
        record.save()
        return JsonResponse({"status": "success"})
    except List.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Record not found."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

class NONO(Exception):
    pass


@csrf_exempt
@hello_decorator
def test(request, name):
    print(name)
    try :
        data=json.loads(request.body)
        body_name = data['name']
        print(body_name)
        raise NONO("nono")
    except NONO as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "success 我只是做測試的別看我"})
