from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Category, Item, List
from utils import hello_decorator
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from django.shortcuts import render


# Create your views here.
#hello world 

def personPage(request):
    return JsonResponse({"status": "success"})


logger = logging.getLogger(__name__)

# 取得分類
@csrf_exempt
def getPersonalCategory(request):
    print("=====================================")
    print(f"Is user authenticated: {request.user.is_authenticated}")
    print(f"User: {request.user}")
    logger.info(f"User: {request.user}")
    logger.info(f"Authenticated: {request.user.is_authenticated}")
    logger.info(f"Session: {request.session.items()}")

    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    data = json.loads(request.body)
    UUID = data.get('UUID')
    categories = Category.objects.filter(UUID=UUID)
    category_list = [{"id": category.id, "name": category.name} for category in categories]

    return JsonResponse({"status": "success", "categories": category_list})  # all data  contain category id and name

# 新增分類
@csrf_exempt
def addCategory(request):
    data = json.loads(request.body)
    name = data.get('name')
    UUID = data.get('UUID')  # user id or something
    category = Category(name=name, UUID=UUID)
    category.save()
    return JsonResponse({"status": "success"})


# 刪除分類
@csrf_exempt
def deleteCategory(request):
    try:
        data = json.loads(request.body)
        id = data.get('id')
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse({"status": "success"})
    except Category.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Category not found."}, status=404)

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
    data = json.loads(request.body)
    category_id = data.get('category_id')  # 用分類id取得所有屬於此分類的健身項目
    category_name = Category.objects.get(id=category_id).name
    items = Item.objects.filter(category=category_id)
    item_list = [{"id": item.id,"name": item.name} for item in items]
    return JsonResponse({"status": "success", "item_list": item_list, "category_name": category_name})


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
        data = json.loads(request.body)
        item_id = data['item_id']
        records = List.objects.filter(item_id=item_id)
        item_name = Item.objects.get(id=item_id).name
        records_list = [{"id": record.id, "name": record.name} for record in records]
        return JsonResponse({"status": "success", "records_list": records_list, "item_name": item_name})
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
def test(request, name, mode):
    if mode == 1:
        age = 30
        string = f"helle{name},you are {age}"
        print(string)
        try:
            data=json.loads(request.body)
            body_name = data['name']
            print(body_name)

        except NONO as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        return JsonResponse({"status": "success 我只是做測試的別看我"})
    else:
        print("template mode")
        companys=["company1","company2","company3"]
        options=["name1","name2","name3"    ]


        items = [
            {'name': 'Apple', 'id': 1, 'category': 'fruit'},
            {'name': 'Banana', 'id': 2, 'category': 'fruit'},
            {'name': 'Carrot', 'id': 3, 'category': 'vegetable'},
        ]
        data={"companys":companys,"options":options,"items":items}
        return render(request, "index.html",data)

