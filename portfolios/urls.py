from django.urls import path
from . import views

app_name = 'portfolios'
urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:year>/<int:month>/<int:day>/<slug:portfolio>', views.portfolio_detail, name='portfolio_detail')
]