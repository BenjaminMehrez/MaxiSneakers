from django.urls import path
from .views import *


urlpatterns = [
    path('', favorite_summary, name='favorite-summary'),
    path('add/', favorite_add, name='favorite-add'),
    path('delete/', favorite_delete, name='favorite-delete'),
]