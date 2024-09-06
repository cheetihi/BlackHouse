from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API. Available endpoints:",
        "endpoints": {
            "candlestick": "/api/candlestick/",
            "line": "/api/line/",
            "bar": "/api/bar/",
            "pie": "/api/pie/"
        }
    })


def home(request):
    return HttpResponse("Welcome to the API! Visit /api/ for the endpoints.")


@api_view(['GET'])
def candlestick_data(request):
    data = {
        "data": [
            {"x": "2024-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
            {"x": "2024-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
        ]
    }
    return Response(data)

@api_view(['GET'])
def line_chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "data": [10, 20, 30, 40]
    }
    return Response(data)

@api_view(['GET'])
def bar_chart_data(request):
    data = {
        "labels": ["Product A", "Product B", "Product C"],
        "data": [120, 180, 250]
    }
    return Response(data)

@api_view(['GET'])
def pie_chart_data(request):
    data = {
        "labels": ["Red", "Blue", "Yellow"],
        "data": [300, 50, 100]
    }
    return Response(data)

# Create your views here.
