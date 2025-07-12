from django.urls import path
from . import views

urlpatterns = [
    path('', views.collage_list, name='collage_list'),
    path('upload/', views.upload_images, name='upload_images'),
    # path('upload_collage/', views.upload_collage, name='upload_collage'),
    path('select/', views.select_images, name='select_images'),
    path('collage/<int:pk>/', views.collage_detail, name='collage_detail'),
]