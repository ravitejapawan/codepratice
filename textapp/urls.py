from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_text, name='delete_text'),
    path('deleted_texts/', views.deleted_texts, name='deleted_texts'),  # View for superusers
]
