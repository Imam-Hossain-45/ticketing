from django.urls import path
from . import views

app_name = 'dh_test'

android_test_urls = [
    path('android/get-user-info/', views.ScanQRView.as_view(), name='user_info'),
    path('android/scan-log/', views.ScanLogListView.as_view(), name='scan_log'),
]

web_test_urls = [
    path('web/get-countries/', views.GetCountryView.as_view(), name='get_countries'),
    path('web/user-event/registration/', views.UserRegistrationView.as_view(), name='user_registration'),
    path('web/registration/list/', views.RegistrationListView.as_view(), name='registration_list'),
    path('web/registration/<registration_id>/detail/', views.RegistrationDetailView.as_view(),
         name='registration_detail'),
]

urlpatterns = android_test_urls + web_test_urls
