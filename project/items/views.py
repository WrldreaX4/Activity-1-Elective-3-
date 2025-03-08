from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

items = []

@require_http_methods(["GET"])
def get_all_items(request):
    search_query = request.GET.get("search", "")
    if search_query:
        filtered_items = [item for item in items if search_query.lower() in item["name"].lower()]
        return JsonResponse({"message": "Filtered Items", "payload": filtered_items}, status=200)
    return JsonResponse({"message": "All Items", "payload": items}, status=200)

@require_http_methods(["GET"])
def get_item(request, item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return JsonResponse({"message": "Item Found", "payload": item}, status=200)
    return JsonResponse({"message": "Item Not Found"}, status=404)

@csrf_exempt
@require_http_methods(["POST"])
def add_item(request):
    try:
        data = json.loads(request.body) if request.body else request.POST
        new_item = {"id": len(items) + 1, "name": data.get("name")}
        items.append(new_item)
        return JsonResponse({"message": "Item Added", "payload": new_item}, status=201)
    except Exception as e:
        return JsonResponse({"message": "Error Adding Item", "error": str(e)}), 400

@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, item_id):
    try:
        data = json.loads(request.body) if request.body else request.POST
        for item in items:
            if item["id"] == item_id:
                item["name"] = data.get("name", item["name"])
                return JsonResponse({"message": "Item Updated", "payload": item}, status=200)
        return JsonResponse({"message": "Item Not Found"}, status=404)
    except Exception as e:
        return JsonResponse({"message": "Error Updating Item", "error": str(e)}), 400

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return JsonResponse({"message": "Item Deleted"}, status=200)
