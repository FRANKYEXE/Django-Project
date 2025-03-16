from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:id>/', views.view_profile, name='view_profile'),
    path('profile/<int:id>/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<int:id>/delete/', views.delete_profile, name='delete_profile'),
]