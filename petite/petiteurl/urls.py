from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:hash>', views.redirect_view, name='redirect'),
]
