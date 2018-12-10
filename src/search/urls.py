from django.urls import path
from .views import SearchProductView

app_name = 'search'
urlpatterns = [
    path('', SearchProductView.as_view(), name='show_searched_product'),
    #path('<int:pk>/', views.ShowItem.as_view(), name='show_one_item'),
    #re_path(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='show_with_slug'),
]
