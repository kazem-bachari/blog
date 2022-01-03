from django import forms
from django.contrib.auth.models import User


class loginform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"Name","class":'form-control my-2 '})
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Password","class":'form-control my-2'})
    )
class registerform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"Name","class":'form-control my-2 '})
    )
    first_name=forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"First Name","class":'form-control my-2 '})
    )
    last_name=forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"Last Name","class":'form-control my-2 '})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": 'form-control my-2'})
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Password","class":'form-control my-2'})
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "re-password", "class": 'form-control my-2'})
    )
    def clean_username(self):
        username=self.cleaned_data['username']
        is_exist_username = User.objects.filter(username=username)
        if is_exist_username:
            raise forms.ValidationError('please choose another username')
        if len(username)<5 :
            raise forms.ValidationError('username are too short')
        if username.isalpha() is False:
            raise forms.ValidationError('just letter character are allowed')
        return username
    def clean_re_password(self):
        password=self.cleaned_data.get('password')
        re_password=self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('passwords must be same')
        return password
