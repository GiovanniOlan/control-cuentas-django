from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('modules.landingpage.urls')),
    path('', include('modules.controlcuentas.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='controlcuentas/user/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
