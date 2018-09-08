from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    #path('show_all_customer/', views.ShowCustomer.as_view(), name='show_all_customer'),
    path('<slug:slug>/', views.ShowCustomer.as_view(), name='show_one_customer'),
]
