from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls'), name='content'),
    path('accounts/', include('users.urls'), name='users'),
]
