from django.conf.urls import url
from .import views
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'articles'

urlpatterns = [
    path('', views.article_list.as_view(), name="list"),    
    re_path(r'^category/(?P<item_id>[0-9]+)/$', views.categorywise_list.as_view(), name="category"),
    path('about/', views.about, name="about"),
    path('results/', views.article_search, name="search"),
    path('sort_like/', views.sort_by_like.as_view(), name="sort_like"),
    path('sort_date/', views.sort_by_date.as_view(), name="sort_date"),
    path('create/', views.article_create.as_view(), name="create"),
    path('<int:pk>/', views.article_detail.as_view(), name="detail"),
    path('<int:pk>/like/', views.article_like_toggle.as_view(), name="like"),
    path('api/<int:pk>/like/', views.article_like_api_toggle.as_view(), name="like-api"),
    path('<int:pk>/edit/',views.article_edit.as_view(), name="edit"),
    path('<int:pk>/delete/', views.article_delete.as_view(), name="delete"),
    re_path(r'^<int:pk>/(?P<pk>[0-9]+)/delete/$', views.comment_delete, name="delete_comment"),
    

]