from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('download_index/', views.download_index, name="download_index"),
    path('api/index-list/', views.IndexView.as_view(), name="index_view"),
    path('table/', views.table, name="table"),
]
