from django.urls import path

from . import views

urlpatterns = [
    path('portfolio_list', views.PortfolioListView.as_view(), name='portfolio_list'),
    path('create_portfolio', views.PortfolioCreateView.as_view(), name='create_portfolio'),
    path('<uuid:pk>', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('<uuid:pk>',views.PortfolioUpdateView.as_view(), name='update_portfolio'),
    path('<uuid:pk>', views.PortfolioDeleteView.as_view(), name='delete_portfolio'),
    path('create_bucket', views.BucketCreateView.as_view(), name='create_bucket'),
    path('bucket_list', views.BucketListView.as_view(), name='bucket_list'),
    path('<uuid:pk>', views.BucketDetailView.as_view(), name='bucket_detail'),
    path('<uuid:pk>', views.BucketUpdateView.as_view(), name='update_bucket'),
    path('<uuid:pk>', views.BucketDeleteView.as_view(), name='delete_bucket'),
]

