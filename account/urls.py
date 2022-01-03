from django.urls import path, include

from account.views import loginForm,registerForm,Edit_information

urlpatterns=[
    path('login', loginForm),
    path('register', registerForm),
    path('edit_user', Edit_information),
]
