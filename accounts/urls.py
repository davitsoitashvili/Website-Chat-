from django.urls import path
from accounts.views import signUpVIew,signInView

urlpatterns = [
    path('', signUpVIew, name='register page'),
    path('login/', signInView, name='login page')
]