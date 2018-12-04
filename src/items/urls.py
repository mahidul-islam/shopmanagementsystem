from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='show_all_item'),
    path('<slug:slug>/', views.ShowItem.as_view(), name='show_one_item'),
    #path('<int:pk>/', views.ShowItem.as_view(), name='show_one_item'),
]
