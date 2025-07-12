from django.contrib.auth.forms import (
    UserCreationForm 
)

from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

