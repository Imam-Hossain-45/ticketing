from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path('get-preferences/', views.GetAllPreferencesView.as_view(), name='get_all_preferences'),
]
