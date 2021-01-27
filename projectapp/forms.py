from django import forms
from .models import ViewerLog,ViewerReg

class WriterForm(forms.Form):
    Title=forms.CharField(
        label="enter title",
        widget=forms.TextInput(
            attrs={
                'class':'from-control',
                'placeholder':'enter title'
            }
        )
    )
    Content=forms.CharField(
        label="enter title",
        widget=forms.Textarea(
            attrs={
                'class':'from-control',
                'placeholder':'enter content'
            }
        )
    )
    image=forms.ImageField()
class ViewRegForm(forms.Form):
    f_name=forms.CharField(
        label="enter your first_name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter fname'
            }
        )
    )
    l_name=forms.CharField(
        label="enter your last_name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter lname'
            }
        )
    )
    username=forms.CharField(
        label="enter your username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter usernaname'
            }
        )
    )
    password=forms.CharField(
        label="enter your password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter password'
            }
        )
    )
class ViewLogForm(forms.Form):
    username=forms.CharField(
        label="enter your username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter usernaname'
            }
        )
    )
    password=forms.CharField(
        label="enter your password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter password'

            }
        )
    )
