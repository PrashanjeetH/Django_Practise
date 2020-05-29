from django import forms

#Create your forms here
class Signupform(forms.Form):
    fname = forms.CharField(max_length = 50)
    mname = forms.CharField(max_length = 50, required=False)
    lname = forms.CharField(max_length = 50)
    no    = forms.IntegerField()
    email = forms.EmailField(help_text = "Enter valid Email address")
    password = forms.CharField(max_length = 200, widget = forms.PasswordInput())
