from django.urls import path
from .views import CategoryApiView, PortfolioApiView




urlpatterns = [
    path('category/', CategoryApiView.as_view(), name='category'),
    path('portfolio/', PortfolioApiView.as_view(), name='portfolio')
]
