from django.contrib import admin
from django.urls import path

from articles import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('article/new', views.create_post, name='create_post'),
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('registration/', views.registration, name='registration'),
    path('admin/', admin.site.urls),
]
