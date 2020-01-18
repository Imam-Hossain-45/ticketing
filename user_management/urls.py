from django.urls import path
from . import views

app_name = 'user_management'


common_urls = [
    path('validate/', views.VisitorRegistrationUsernameCheckView.as_view(), name='username_validate'),
]

visitor_urls = [
    path('visitor/create/', views.VisitorRegistrationView.as_view(), name='visitor_create'),
    path('visitor/profile/', views.VisitorRegistrationView.as_view(), name='visitor_profile'),
    path('visitor/<user_id>/profile/change-profile-picture/', views.ChangeProfilePictureView.as_view(),
         name='visitor_profile_picture_change'),
    path('visitor/preferences/', views.VisitorRegistrationView.as_view(), name='visitor_preferences'),
]

business_urls = [
    path('business/create/', views.VisitorRegistrationView.as_view(), name='business_create'),
]

urlpatterns = common_urls + visitor_urls + business_urls
