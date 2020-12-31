from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    contactView,
    PrivacyPolicyView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contactView, name='contact'),
    path(
        'privacy-policy/',
        PrivacyPolicyView.as_view(),
        name='privacy_policy'
    ),
]