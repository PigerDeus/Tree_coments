from django.urls import include, path
from . import views

urlpatterns = [

    path('posts/', views.posts, name='posts'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', views.index, name='login'),
]
