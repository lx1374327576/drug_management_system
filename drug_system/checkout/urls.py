from django.urls import path

from . import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('make/', views.make, name='make'),
    path('submit/', views.submit, name='submit'),
    path('query/', views.query, name='query'),
    path('query_detail/<int:checkout_id>/', views.query_detail, name='query_detail'),
    path('query/<int:page_id>/', views.query_page, name='query_page'),
    path('move/<int:checkout_id>/', views.move, name='move'),
]
