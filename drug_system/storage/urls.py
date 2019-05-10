from django.urls import path

from . import views

app_name = 'storage'

urlpatterns = [
    path('storage/', views.storage, name='storage'),
    path('submit/', views.submit, name='submit'),
    path('make/', views.make, name='make'),
    path('query/', views.query, name='query'),
    path('query_detail/<int:storage_id>/', views.query_detail, name='query_detail'),
    path('accept/<int:storage_id>/', views.accept, name='accept'),
    path('deny/<int:storage_id>/', views.deny, name='deny'),
    path('move/<int:storage_id>', views.move, name='move'),
]
