from email import message
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Sign_in
from .models import Student
from .forms import StudentForm
from .forms import Sign_inForm
from django.forms import ModelForm, ValidationError


new_company_code=0;

# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

# def index_sign(request):
#       return render(request, 'students/sign_in.html', {
#     # 'students': Student.objects.all()
#   })
# def loginto(request,id):
#       idx=0
     
#       submitit=request.POST.get('company_submit')
      
#       print(submitit)

#       if(submitit):
#             new_username=request.POST.get('_Username')
#             new_company_code=request.POST.get('Company_Code')
#             new_company_Name=request.POST.get('Company_Name')
#             sign_in = Sign_in.objects.all()
#             for k in sign_in:
#                 if k.user_name==new_username and k.company_code==new_company_code and k.company_name==new_company_Name:
#                       idx=k.id
#                       flag=True
#                 else:
#                       flag=False
#             if flag:
#                   edit_emply(idx)
#             else:
#                   return render(request, 'students/forgot.html', {
                  
#                   'error': True,
#                   'msg':'There is not  company  with  yours username'
#                   })
                  
#       else:
#                   # new_sign_in = Sign_in.objects.get(pk=idx)
#                   # form = Sign_inForm(instance=new_sign_in)
#                   return render(request, 'students/forgot.html'
#                 )

                  
                  
            # return HttpResponseRedirect(reverse('Login_form'))
def forgot(request):
      
      idx=0
     
      submitit=request.POST.get('company_submit')
      
      print(submitit)

      if(submitit):
            new_username=request.POST.get('_Username')
            new_company_code=request.POST.get('Company_Code')
            new_company_Name=request.POST.get('Company_Name')
            sign_in = Sign_in.objects.all()
            for k in sign_in:
                if k.user_name==new_username and k.company_code==new_company_code and k.company_name==new_company_Name:
                      idx=k.company_code
                      flag=True
                else:
                      flag=False
            if flag:
                  # edit_emply(request,new_company_code)
                  valuereurn(new_company_code)
                 
                  
                  
            else:
                  return render(request, 'students/forgot.html', {
                  
                  'error': True,
                  'msg':'There is not  company  with  yours username'
                  })
                  
      else:
                  # new_sign_in = Sign_in.objects.get(pk=idx)
                  # form = Sign_inForm(instance=new_sign_in)
                  return render(request, 'students/forgot.html'


                )
def valuereurn(x):
      return x


def edit_emply( request,new_company_code):
                 
          
      
                    new_Sign_in = Sign_in.objects.get.objects.get(pk=new_company_code)
                    form = Sign_inForm(request.POST, instance=new_Sign_in)
                    if form.is_valid():
                      form.save()
                      return render(request, 'students/edit_employees.html', {
                      'form': form,
                      'success': True
                    })
                    else:
                           new_Sign_in = Sign_in.objects.get(pk=new_company_code)
                  
                           new_Sign_in = Sign_in.objects.get(pk=new_company_code)
                            
                           form = StudentForm(instance=new_Sign_in)
                            
                           return render(request, 'students/edit_employees.html', {
                            'form': form
                          })
                 
                     

      

      
            
      
def Login_form(request):
       count=0
       submitit=request.POST.get('login_submit')
       if(submitit):
          new_username=request.POST.get('int_Username')
          new_password=request.POST.get('int_password')
          sign_in = Sign_in.objects.all()
          for k in sign_in:
                if k.user_name==new_username and k.password_of_user==new_password:
                      count=count+1

          if count<=0:
                return render(request, 'students/login.html', {
                  
                  'error': True,
                  'msg':'Username and Password match'
                  })
          else:
                 return render(request, 'students/index.html')
                
            
          

       else:
            return render(request, 'students/login.html')
            
def view_student(request, id):
  student = Student.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_date_of_birth = form.cleaned_data['date_of_birth']
      new_last_name = form.cleaned_data['last_name']
      new_temporary_address = form.cleaned_data['temporary_address']
      new_phone_number = form.cleaned_data['phone_number']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_level_of_study = form.cleaned_data['level_of_study']
      new_university_or_board = form.cleaned_data['university_or_board']
      new_gpa = form.cleaned_data['gpa']
      new_country_to_apply = form.cleaned_data['country_to_apply']

      new_student = Student(
        student_number = new_student_number,
        first_name = new_first_name,
        date_of_birth=new_date_of_birth,
        last_name = new_last_name,
        temporary_address=new_temporary_address,
        phone_number=new_phone_number,
        email = new_email,
        field_of_study = new_field_of_study,
        level_of_study=new_level_of_study,
        university_or_board=new_university_or_board,
        gpa = new_gpa,
        country_to_apply=new_country_to_apply
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })

def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
def Sign_in_for_user(request):
  
  if request.method == 'POST':
     
     form = Sign_inForm(request.POST) 
     if form.is_valid():
    
      if form.cleaned_data['password_of_user']==form.cleaned_data['confirm_password'] :
          new_emply_name = form.cleaned_data['emply_name']
          new_company_code = form.cleaned_data['company_code']
          new_company_name = form.cleaned_data['company_name']
          new_user_name = form.cleaned_data['user_name']
          new_email = form.cleaned_data['email']
          new_password_of_user = form.cleaned_data['password_of_user']
          new_confirm_password = form.cleaned_data['confirm_password']
          
          
          new_sign_in = Sign_in(
                  emply_name = new_emply_name,
                  company_code = new_company_code,
                  company_name = new_company_name,
                  user_name=new_user_name,
                  email = new_email,
                  password_of_user=new_password_of_user,
                  confirm_password=new_confirm_password
                )
          new_sign_in.save()

          return render(request, 'students/sign_in.html', {
                  'form': Sign_inForm(),
                  'success': True
                  })
      else:
            
            return render(request, 'students/sign_in.html', {
                  'form': Sign_inForm(),
                  'error': True,
                  'msg':' Incorret Password and Confirm Password'
                  })
     else:
          return render(request, 'students/sign_in.html', {
                  'form': Sign_inForm(),
                  'error': True,
                  'msg':'Form Is Not valied'
                  })
          
              
          
  else:
         form = Sign_inForm()
         return render(request, 'students/sign_in.html', {
         'form': Sign_inForm()
         })
          
          #  fields = ['emply_name', 'company_code','company_name' ,'user_name','email','password_of_user' ]
