from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('username-check/', views.VisitorRegistrationUsernameCheckView.as_view(), name='username_check'),
    path('visitor/create/', views.VisitorRegistrationView.as_view(), name='visitor_create'),
]
