from django.urls import path
from . import views

urlpatterns = [
    path('connect-vibes/', views.HomePage, name='home'),
    path('discovery/', views.DiscoveryPage, name='discovery'),
    path('social_networking/', views.SocialNetworking, name='social_page'),
    path('business_promotion/', views.BusinessPage, name='business'),
    path('virtual_closet/', views.VirtualClosetPage, name='virtual_closet'),
]