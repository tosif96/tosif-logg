from django.contrib import admin
from django.urls import path
from . import views

# Code for video 6
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),

]