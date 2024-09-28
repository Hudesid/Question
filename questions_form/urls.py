from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_form_view, name='main'),
    path('success', views.success_view, name='success'),
    path('questions/list', views.question_list_view, name='list')
]