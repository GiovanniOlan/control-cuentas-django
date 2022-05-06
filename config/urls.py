from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', include('modules.landingpage.urls')),
    path('', include('modules.controlcuentas.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='controlcuentas/user/login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
]
