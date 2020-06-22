from django.urls import path,include
from . import views

urlpatterns = [
    path('crawl/', views.index, name="index"),
]
