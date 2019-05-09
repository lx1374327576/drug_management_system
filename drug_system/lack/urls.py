from django.urls import path

from . import views

app_name = 'lack'

urlpatterns = [
    path('lack/', views.lack, name='lack'),
]
