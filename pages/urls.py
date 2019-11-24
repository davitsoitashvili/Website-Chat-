from django.urls import path
from pages.views import mainView,logoutView


urlpatterns = [
    path('', mainView, name="main page"),
    path('logout/', logoutView, name='logout')
]