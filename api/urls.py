from django.urls import path,re_path
from . import views

urlpatterns = [
    path('<int:id>/',views.index,name="index"),
    path('id/',views.id,name="id")
]