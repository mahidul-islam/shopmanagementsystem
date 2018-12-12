from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [

    path('', views.ProductListView.as_view(), name='show_all_product'),
    path('featured/', views.FeaturedProductListView.as_view(), name='show_all_featured_product'),
    path('featured/<int:pk>/', views.FeaturedProductDetailView.as_view(), name='show_one_featured_product'),
    #this url must be under fearured else the featured word is treated as a slug and product not found
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='show_one_product'),
    #path('<int:pk>/', views.ShowItem.as_view(), name='show_one_item'),
    #re_path(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='show_with_slug'),
]
