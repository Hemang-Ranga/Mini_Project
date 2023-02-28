from django.urls import path
from . import views

app_name='dict_pad'

urlpatterns = [
    path('', views.first_page, name='first'),
    path('dictation/', views.second_page, name='second'),
    path('download/', views.download, name='download')
]
