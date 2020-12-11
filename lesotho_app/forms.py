from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Claims


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ['claimant', 'claimant_title', 'claimant_first_name', 'claimant_last_name',
                  'claimant_phone_number', 'claimant_policy_number', 'claimant_email', 'claimant_id_number',
                  'claimant_passport_number', 'claimant_physical_address', 'claimant_postal_address', 'claimant_age',
                  'claimant_relationship', 'deceased_title', 'deceased_first_name', 'deceased_last_name', 'deceased_date_of_birth',
                  'deceased_place_of_birth', 'deceased_date_of_death', 'deceased_time_of_death', 'deceased_age_of_death', 'deceased_cause_of_death',
                  'deceased_place_of_death', 'deceased_passport_number', 'deceased_id_number', 'deceased_marital_status',
                  'deceased_physical_address', 'deceased_postal_address']