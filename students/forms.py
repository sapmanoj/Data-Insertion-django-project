from django import forms 
from .models import Student
from .models import Sign_in


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name','date_of_birth', 'last_name','temporary_address' ,'phone_number','email', 'field_of_study','level_of_study','university_or_board', 'gpa','country_to_apply']
    labels = {
      'student_number': 'Student Number', 
      'first_name': ' Student Name',
      'date_of_birth':'Birth Date',
      'last_name': 'Parmanent Address', 
      'temporary_address': 'Temporary Address' ,
      'phone_number':'Phone Number',
      'email': 'Email', 
      'field_of_study': 'Field of Study', 
      'level_of_study': 'Current  Degree level',
      'university_or_board':'University or Board oF Degree',

      'gpa': 'GPA',
      'country_to_apply':'Country Apply',
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'temporary_address': forms.TextInput(attrs={'class': 'form-control'}),
      'phone_number': forms.NumberInput(attrs={'class': 'form-control'}), 
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'level_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'university_or_board': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
      'country_to_apply': forms.TextInput(attrs={'class': 'form-control'}),
    }
class Sign_inForm(forms.ModelForm):
  class Meta:
    model = Sign_in
    
    fields = ['emply_name', 'company_code','company_name' ,'user_name','email','password_of_user' ,'confirm_password']
    labels = {
      'emply_name': 'Employee Name', 
      'company_code': 'Company Code',
      'company_name':'Company Name',
      'user_name': 'User Name', 
      'email': 'Email' ,
      'password_of_user':'Password',
      'confirm_password':'Confirm Password' ,
     }
    widgets = {
      'emply_name': forms.TextInput(attrs={'class': 'form-control'}), 
      'company_code': forms.TextInput(attrs={'class': 'form-control'}),
      'company_name': forms.TextInput(attrs={'class': 'form-control'}),
      'user_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'password_of_user': forms.PasswordInput(attrs={'class': 'form-control'}),
      'confirm_password': forms.PasswordInput(attrs={'class': 'form-control'}),
      }