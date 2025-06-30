from django import forms
from .models import User, Record

class UserCreationForm(forms.ModelForm):
    login = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    def check_password(self):
        user_password1 = self.cleaned_data['password1']
        user_password2 = self.cleaned_data['password2']

        return user_password1 == user_password2
    
    class Meta:
        model = User
        fields = ['username','name','email','password']


class RecordCreationForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'text', 'author']