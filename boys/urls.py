from django.urls import path
from . import views

urlpatterns = [
    path('boys/', views.BoysListAPIView.as_view(), name='boys'),
    path('boys/<str:pk>/', views.BoysUpdateAPIView.as_view(), name='boys'),
    path('boys/crud/<str:pk>/', views.BoysCRUDAPIView.as_view(), name='boys')
]
