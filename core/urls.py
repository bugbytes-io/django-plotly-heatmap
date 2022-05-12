from django.urls import include, path
from . import views

urlpatterns = [
    path('commits/', views.commits, name='commits')
]