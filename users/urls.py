from django.urls import path
from .views import *

urlpatterns = [
    path('application/', SponsorApplicationView.as_view(), name='application'),
    path('sponsor/', SponsorListView.as_view(), name='sponsor'),
    path('profile/<int:pk>/', SponsorProfileView.as_view(), name='profile'),
    path('student/register/', StudentRegisterView.as_view(), name='student'),
    path('student/', StudentListView.as_view(), name='student'),
    path('student/<int:pk>/', StudentProfileView.as_view(), name='student'),
    path('student/paid/', PaidBudgetView.as_view(), name='student_paid'),
]
