import email
from email.policy import default
# from ssl import _PasswordType
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField(default=1)
  first_name = models.CharField(max_length=500)
  date_of_birth=models.DateField(default = None)
  last_name = models.CharField(max_length=500)
  temporary_address=models.CharField(max_length=500,default = None)
  phone_number=models.PositiveIntegerField(default=None)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=500)
  level_of_study=models.CharField(max_length=500,default = None)
  university_or_board=models.CharField(max_length=500,default = None)
  gpa = models.FloatField()
  country_to_apply=models.CharField(max_length=200,default = None)

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'

class Sign_in(models.Model):
      emply_name=models.CharField(max_length=500)
      company_code= models.CharField(primary_key=True,max_length=6)
      company_name=models.CharField(max_length=500)
      user_name= models.CharField(max_length=500)
      email= models.EmailField(max_length=100)
      password_of_user=models.CharField(max_length=500)
      confirm_password=models.CharField(max_length=500,blank=True)
      def __str__(self):
        return f'Sign_in: {self.company_code} {self.company_name}'
       
       
       
  
