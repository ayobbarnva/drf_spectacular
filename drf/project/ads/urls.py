from django.urls import path
from . import views


app_name = 'ads'
urlpatterns = [
     path('all', views.AdListView.as_view(), name='ad_list'),
     path('add', views.creat_ad_post.as_view(), name='ad_create'),
     path('<int:pk>', views.detail_ad.as_view(), name='ad_detail'),
     path('serach/',views.ad_search.as_view())
]