from django.urls import path, include
from . import views

urlpatterns = [
    path('upload', views.UploadView.as_view()),
    path('hwkid', views.HwkView.as_view())
]