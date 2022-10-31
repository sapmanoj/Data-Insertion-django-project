from django.urls import path
from . import views


urlpatterns = [
  path('index/', views.index, name='index'),
  path('', views.Login_form, name='Login_form'),
  # path('sign_in/', views.index_sign, name='index_sign'),
  path('Sign_in_for_user/', views.Sign_in_for_user, name='Sign_in_for_user'),
  # path('loginto/', views.Login_form, name='loginto'),
  path('forget', views.forgot, name='forgot'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('editemploye/', views.edit_emply, name='edit_emply'),
  path('delete/<int:id>/', views.delete, name='delete'),
]