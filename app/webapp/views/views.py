import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def add_view(request, *args, **kwargs):
    data = {
        'A': 1234,
        'B': 4567,
    }
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] + data['B']})
    return response


def subtract_view(request, *args, **kwargs):
    data = {
        'A': 1234,
        'B': 4567,
    }
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] - data['B']})
    return response


def multiply_view(request, *args, **kwargs):
    data = {
        'A': 1234,
        'B': 4567,
    }
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] * data['B']})
    return response


def divide_view(request, *args, **kwargs):
    data = {
        'A': 1234,
        'B': 4567,
    }
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    elif data['B'] == 0:
        response = JsonResponse({"error": "Division by zero"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] / data['B']})
    return response
