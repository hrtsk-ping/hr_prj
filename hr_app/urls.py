from django.urls import path

from . import views

app_name = 'hr_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('job_list/', views.JobListView.as_view(), name='job_list'),
    path('job_post/', views.JobPostView.as_view(), name='job_post'),
]