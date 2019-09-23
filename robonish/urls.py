from django.urls import path
from django.conf.urls import url
from . import views

app_name = "robonish"

urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('register/<int:id>/', views.register_view_id, name='register_view_id'),
]