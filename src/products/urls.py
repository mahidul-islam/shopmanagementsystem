from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='show_all_item'),
    path('<slug:slug>/', views.ShowItem.as_view(), name='show_one_item'),
    #path('<int:pk>/', views.ShowItem.as_view(), name='show_one_item'),
    #re_path(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='show_with_slug'),
]
