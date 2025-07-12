from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_images, name='upload_images'),
    # path('upload_collage/', views.upload_collage, name='upload_collage'),
    path('select/', views.select_images, name='select_images'),
    path('collage/<int:pk>/', views.collage_detail, name='collage_detail'),
]
