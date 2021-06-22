from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('cookbook/', include('cookbook.urls')),
    path('private/', include('private.urls')),
]
