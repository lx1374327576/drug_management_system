from django.urls import path

from . import views

app_name = 'lack'

urlpatterns = [
    path('lack/', views.lack, name='lack'),
    path('make/', views.make, name='make'),
    path('submit/', views.submit, name='submit'),
    path('query/', views.query, name='query'),
    path('query_detail/<int:lack_id>', views.query_detail, name='query_detail'),
]
