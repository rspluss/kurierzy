from django.urls import path
from . import views

app_name = "gpw"

urlpatterns = [
    path('', views.home, name="home"),
    path('download_index/', views.download_index, name="download_index"),
]
