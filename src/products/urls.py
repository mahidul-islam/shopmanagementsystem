from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='show_all_product'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='show_one_product'),
    #path('<int:pk>/', views.ShowItem.as_view(), name='show_one_item'),
    #re_path(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='show_with_slug'),
]
