from django.urls import path, include

from account.views import loginForm,registerForm

urlpatterns=[
    path('login', loginForm),
    path('register', registerForm),
]
