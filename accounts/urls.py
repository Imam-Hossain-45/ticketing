from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
]
