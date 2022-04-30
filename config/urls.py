from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('modules.landingpage.urls')),
    path('controlcuentas/', include('modules.controlcuentas.urls')),
    path('admin/', admin.site.urls),
]
