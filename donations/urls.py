from django.urls import path
from .views import DonationsPageView


app_name = 'donations'
urlpatterns = [
    path('', DonationsPageView.as_view(), name='donations'),
]