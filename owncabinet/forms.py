from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import OwnCabinet


# class ChangeUserInfoForm(forms.ModelForm):
#     email = forms.EmailField(required=True, label='Адрес электронной почты')
#
#     class Meta:
#         model = OwnCabinet
#         fields = ('username', 'email', 'first_name', 'last_name',
#                   'send_messages')


class RegisterUserForm(forms.ModelForm):
    # email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password (one more time)',
                                widget=forms.PasswordInput,
                                help_text='Enter the same password one more time')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Passwords mismatch', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = OwnCabinet
        fields = ('username', 'password1', 'password2')
