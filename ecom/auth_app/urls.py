from django.urls import path
from . import views

urlpatterns = [
    path('home/', view = views.home, name = 'home'),
    path('', view=views.login, name = 'login'),
    path('register/', view = views.register, name = 'register'),
    path('check_email/', view=views.check_email, name = 'check_email'),
    path('reset_password/<str:email>', view = views.reset_password, name = 'reset_password')
]