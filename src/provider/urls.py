from django.urls import path
from . import views

app_name = 'provider'
urlpatterns = [
    #path('show_all_provider/', views.ShowProvider.as_view(), name='show_all_provider'),
    path('<slug:slug>/', views.ShowProvider.as_view(), name='show_one_provider'),
]
