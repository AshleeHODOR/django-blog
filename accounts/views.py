from django.shortcuts import render 
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm 

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm    #added Customs
    success_url = reverse_lazy("login")

