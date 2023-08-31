from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

USER_TYPE = (
    ('Client', 'Client'),
    ('VipClient', 'VipClient'),
    ('BigBoss', 'BigBoss')
)

GENDER = (
    ('M', 'M'),
    ('Ж', 'Ж')
)

class CustomUserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "age",
            "gender",
            "user_type",
        )
    def save(self, commit=True):
        user = super(CustomUserRegistration,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


