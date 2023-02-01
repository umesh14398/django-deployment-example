from django.urls import path
from basic_app import views

#Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('basic/', views.basic, name='basic'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
