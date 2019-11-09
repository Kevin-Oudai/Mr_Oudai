from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    middle_name = forms.CharField(max_length=30, label="Middle Name")
    phone = forms.CharField(max_length=30, label="Phone Number")

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user