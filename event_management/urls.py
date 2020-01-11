from django.urls import path
from . import views

app_name = 'event_management'

urlpatterns = [
    path('get-all/', views.VisitorRegistrationView.as_view(), name='event_get_all'),
    path('get-nearby/', views.VisitorRegistrationView.as_view(), name='event_nearby'),
    path('get-preferred/', views.VisitorRegistrationView.as_view(), name='event-preferred'),
]
