from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fullname = forms.CharField(label = "Name", required=True)

    class Meta:
        model = User
        fields = ("username", "email" ,"fullname", "password1", "password2")

    def save(self, commit=True):       
        user = super(RegistrationForm, self).save(commit=False)
        user.fullname = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user