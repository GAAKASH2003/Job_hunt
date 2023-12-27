from .models import *
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *
from django import forms
from django.core.validators import FileExtensionValidator



# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_student', 'is_tnp')


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
        
    def __init__(self, *args, **kwargs):
      super(UserCreateForm, self).__init__(*args, **kwargs)

      for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
             


class addinfoform(forms.ModelForm):
    # pdf_file = forms.FileField(
    #     label='Select a PDF file',
    #     validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    # )
    class Meta:
        model=addinfo
        fields=('phone','file','work_place','designation','job_role','codechef_username','leetcode_username','gfg_username','codeforces_username','github_username')
    
class compannform(forms.ModelForm):
    class Meta:
        model=compann
        fields=('company_name','offer_type','eligible_branches','eligibility_criteria','Job_title','salary','deadline','jd')   
    

class applyform(forms.ModelForm):
    class Meta:
        model=comapply
        fields=('name','Degree','Branch','cgpa','email','roll_no','phone_no','file')
                  