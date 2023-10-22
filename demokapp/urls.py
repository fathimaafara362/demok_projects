from . import views
from django.urls import path, include



urlpatterns = [

    path('',views.desk,name='desk')
]