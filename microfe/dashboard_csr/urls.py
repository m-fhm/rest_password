from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reset', views.user_password_rest_through_dashboard, name='reset'),
    path('poll', views.allow_polls_public, name='poll'),
    path('survey', views.get_user_survey_questions, name='get_survey'),
]