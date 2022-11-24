from django.contrib import admin
from django.urls import path, include
from .yasg import yasgi_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('drf-auth/', include('rest_framework.urls')),
]

urlpatterns += yasgi_urlpatterns
