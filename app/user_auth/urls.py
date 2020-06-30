from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('reset_password/',
         views.PasswordResetView.as_view(
             template_name='user_auth/password_reset.html',
             subject_template_name='user_auth/password_reset_subject.txt',
             html_email_template_name='user_auth/password_reset_email.html',
             ),
         name='reset_password'),
    path('reset_password_sent/',
         views.PasswordResetDoneView.as_view(template_name='user_auth/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='user_auth/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         views.PasswordResetCompleteView.as_view(template_name='user_auth/password_reset_complete.html'),
         name='password_reset_complete'),
]