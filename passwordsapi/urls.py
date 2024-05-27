from django.urls import path
from .views import password_page
urlpatterns = [
    path("passwords/",password_page,name="passwords")
]