from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='home'),
    path('video/list/', views.VideoList.as_view(), name='video-list'),
    path('video/detail/<int:pk>/', views.VideoDetail.as_view(), name='video-detail'),
    path('video/list/category/<int:pk>/', views.category_list, name='video-category-list'),
    path('video/search/', views.SearchView.as_view(), name='search-video'),
    path('aboutus/', views.AboutUs.as_view(), name='about'),
]