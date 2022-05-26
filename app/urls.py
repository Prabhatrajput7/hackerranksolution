from django.urls import path
from . import views

urlpatterns = [
    path('',views.Pageone.as_view(), name='main'),
    path('task_view/',views.Pagetwo.as_view(), name='tv'),
    path('cross/<int:id>/',views.complete, name='com'),
    path('uncross/<int:id>/',views.uncomplete, name='un')
]
