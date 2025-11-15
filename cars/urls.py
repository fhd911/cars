from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ⭐ ربط التطبيقات الثلاثة
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('orders/', include('orders.urls')),

    # ⭐ الصفحة الرئيسية (الصفحة الافتراضية)
    path('', include('store.urls')),
]
