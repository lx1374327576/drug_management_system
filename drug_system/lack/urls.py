from django.urls import path

from . import views

app_name = 'lack'

urlpatterns = [
    path('lack/', views.lack, name='lack'),
    path('make/', views.make, name='make'),
    path('submit/', views.submit, name='submit'),
    path('query/', views.query, name='query'),
    path('query/<int:page_id>', views.query_page, name='query_page'),
    path('stack/', views.stack, name='stack'),
    path('query_detail/<int:lack_id>', views.query_detail, name='query_detail'),
    path('stack_submit/', views.stack_submit, name='stack_submit'),
]
