from django.urls import path
from .views import candlestick_data, line_chart_data, bar_chart_data, pie_chart_data, api_root

urlpatterns = [
    path('', api_root),
    path('candlestick/', candlestick_data),
    path('line/', line_chart_data),
    path('bar/', bar_chart_data),
    path('pie/', pie_chart_data),
]
