from django.urls import path
from . import views

app_name = 'ticket_management'

urlpatterns = [
    # path('<user>/get-tickets/', views.VisitorRegistrationView.as_view(), name='user_all_tickets'),
    # path('<user>/get-ticket/<event>', views.VisitorRegistrationView.as_view(), name='user_event_ticket'),
    # path('validate/', views.VisitorRegistrationView.as_view(), name='ticket_validation'),
]
