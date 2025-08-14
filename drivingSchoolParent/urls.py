from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Admin access
    path('', include('main.urls')),   # main app
    path('appointment/', include('appointment.urls')),  # appointments
]