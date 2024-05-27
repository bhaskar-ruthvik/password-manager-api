from django.shortcuts import render, HttpResponse
# Create your views here.
def password_page(request):
    return HttpResponse("Password Page!")