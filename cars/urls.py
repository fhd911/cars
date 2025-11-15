from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ⭐ ربط التطبيقات الثلاثة
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('orders/', include('orders.urls')),

    # ⭐ الصفحة الرئيسية (store هي الافتراضية)
    path('', include('store.urls')),
]

# ⭐ دعم ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
