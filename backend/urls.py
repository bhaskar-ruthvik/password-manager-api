from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/",include("authapi.urls")),
    path("user/",include("passwordsapi.urls")),
    path("auth-api",include("rest_framework.urls"))
]
