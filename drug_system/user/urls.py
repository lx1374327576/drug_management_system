from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    path('demand/', views.demand, name='demand'),
    path('checkout/', views.checkout, name='checkout'),
    path('lack/', views.lack, name='lack'),
    path('purchase/', views.purchase, name='purchase'),
    path('storage/', views.storage, name='storage'),
    path('login/', views.login, name='login'),
    path('<int:id>/<str:query_name>/', views.query, name='query'),
]
