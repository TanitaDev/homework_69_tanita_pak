from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

data = {
    "A": 1234,
    "B": 4567,
}


def add_view(request, *args, **kwargs):
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] + data['B']})
    return response


def subtract_view(request, *args, **kwargs):
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] - data['B']})
    return response


def multiply_view(request, *args, **kwargs):
    if type(data['A']) != int or type(data['B']) != int:
        response = JsonResponse({"error": "Not integer"})
        response.status_code = 400
        return response
    else:
        response = JsonResponse({'answer': data['A'] * data['B']})
    return response


def divide_view(request, *args, **kwargs):
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


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class IndexView(TemplateView):
    template_name = 'index.html'
