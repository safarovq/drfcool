from django.urls import path
from . import views

urlpatterns = [
    path('boys/', views.BoysView.as_view(), name='boys')
]
