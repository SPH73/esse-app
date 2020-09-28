from django.urls import path

from .views import (PortfolioListView, 
                    PortfolioDetailView,
                    BucketListView, 
                    BucketDetailView)

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio-list'),
    path('<uuid:pk>', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('', BucketListView.as_view(), name='bucket-list'),
    path('<uuid:pk>', BucketDetailView.as_view(), name='bucket-detail')
]

