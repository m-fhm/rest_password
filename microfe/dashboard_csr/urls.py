from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reset', views.user_password_rest_through_dashboard, name='reset'),
]