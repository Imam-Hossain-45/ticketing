from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('user/', include('user_management.urls', namespace='user_management')),
    path('event/', include('event_management.urls', namespace='event_management')),
    path('ticket/', include('ticket_management.urls', namespace='ticket_management')),
    path('settings/', include('settings.urls', namespace='settings')),
    path('test/', include('dh_test.urls', namespace='dh_test')),
]
