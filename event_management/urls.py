from django.urls import path
from . import views

app_name = 'event_management'

urlpatterns = [
    path('create/', views.EventCreateView.as_view(), name='create_new_event'),
    path('venue/create/', views.VenueCreateView.as_view(), name='create_new_venue'),
    path('get-all-list/', views.EventListAllView.as_view(), name='get_all_event'),
    # path('get-nearby/', views.VisitorRegistrationView.as_view(), name='event_nearby'),
    # path('get-preferred/', views.VisitorRegistrationView.as_view(), name='event-preferred'),
]
