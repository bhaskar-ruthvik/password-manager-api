from django.urls import path
from .views import CreatePasswordView, DeletePasswordView
urlpatterns = [
    path("passwords/",CreatePasswordView.as_view(),name="passwords"),
    path("passwords/delete/<int:pk>/",DeletePasswordView.as_view(),name="delete_password")
]