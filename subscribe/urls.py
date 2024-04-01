from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.SubscribeView.as_view(), name='subscribe'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'),
]