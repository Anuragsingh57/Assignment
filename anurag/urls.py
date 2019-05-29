from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('task1', views.task1, name='task1'),
   path('task1.1', views.task1_1, name='task1.1'),
   path('task2', views.task2, name='task2'),
   path('task3', views.task3, name='task3'),
]