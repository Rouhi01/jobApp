from django.urls import path
from . import views\

app_name = 'app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('job_detail/<int:job_id>/', views.JobDetailView.as_view(), name='job_detail'),
]