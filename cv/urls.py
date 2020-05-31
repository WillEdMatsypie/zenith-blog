from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cv, name='cv'),
    path('education/new/', views.education_new, name='education_new'),
    path('education/<int:pk>/remove/', views.education_remove, name='education_remove'),
]