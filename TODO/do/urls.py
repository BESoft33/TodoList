from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='list'),
    path('update/<int:pk>', views.update, name='update' ),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('check/<int:pk>', views.check, name='check')
]