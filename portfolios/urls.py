from django.urls import path

from .views import (PortfolioCreateView,
                    PortfolioListView,
                    PortfolioDetailView,
                    PortfolioUpdateView,
                    PortfolioDeleteView,
                    BucketCreateView,
                    BucketListView, 
                    BucketDetailView,
                    BucketUpdateView,
                    BucketDeleteView)

urlpatterns = [
    path('', PortfolioCreateView.as_view(), name='create_portfolio'),
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('<uuid:pk>', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('<uuid:pk>', PortfolioUpdateView.as_view(), name='update_portfolio'),
    path('<uuid:pk>', PortfolioDeleteView.as_view(), name='delete_portfolio'),
    path('', BucketCreateView.as_view(), name='create_bucket'),
    path('', BucketListView.as_view(), name='bucket_list'),
    path('<uuid:pk>', BucketDetailView.as_view(), name='bucket_detail'),
    path('<uuid:pk>', BucketUpdateView.as_view(), name='update_bucket'),
    path('<uuid:pk>', BucketDeleteView.as_view(), name='delete_bucket'),
]

