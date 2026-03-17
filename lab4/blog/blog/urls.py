from django.contrib import admin
from django.urls import path

from articles import views

urlpatterns = [
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('admin/', admin.site.urls),
]
