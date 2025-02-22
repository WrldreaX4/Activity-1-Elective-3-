from django.urls import path
from .views import index
from .views import dashboard


app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
]
