from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('controlcuentas/', include('controlcuentas.urls')),
    path('', include('landingpage.urls')),
    path('admin/', admin.site.urls),
]
