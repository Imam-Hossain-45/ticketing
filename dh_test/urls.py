from django.urls import path
from . import views

app_name = 'dh_test'

android_test_urls = [
    path('android/get-user-info/', views.ScanQRView.as_view(), name='user_info'),
    path('android/scan-log/', views.ScanLogListView.as_view(), name='scan_log'),
]

urlpatterns = android_test_urls
