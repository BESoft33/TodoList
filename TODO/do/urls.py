from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='list'),
    path('update/<str:pk>', views.update, name='update' )
]