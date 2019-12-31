from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('visitor/create/', views.VisitorRegistrationView.as_view(), name='visitor_create'),
]
