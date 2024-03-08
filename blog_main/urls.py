
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('details/<int:id>/',views.details,name="details"),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('search/', views.search, name='search'),
    path('post/<int:id>/like/', views.like_post, name='like_post'),
    path('post/<int:id>/dislike/',views.dislike_post,name='dislike_post'),
    path('create/',views.create_post,name= 'create_post'),
    path('post/<int:id>/delete/',views.delete_post,name='delete_post'),
   
]
