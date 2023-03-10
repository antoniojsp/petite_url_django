from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:hashing>', views.redirect_view, name='redirect_view'),
    path('is_hash_used/', views.is_hash_used, name='is_hash_used'),
]
