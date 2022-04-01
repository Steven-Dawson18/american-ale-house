"""Checkout Urls"""
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('checkout_summary/', views.checkout_summary, name='checkout_summary'),
    path('add_coupon/', views.AddCouponView.as_view(), name='add_coupon'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
