from django.urls import path
from .views import *

urlpatterns = [
    path('application/', SponsorApplicationView.as_view(), name='application'),
    path('list/', SponsorListView.as_view(), name='list'),
    path('profile/<int:pk>/', SponsorProfileView.as_view(), name='profile'),
]
