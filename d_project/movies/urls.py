from django.urls import path
from . import views
app_name = "movies"
urlpatterns = [
    path('', views.movies_list, name='home'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.movies_detail, name='detail'),
    path('<slug:slug>/like', views.like_view, name='like'),
    path('<slug:slug>/review', views.sub_review, name='review'),



]
