from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_dars import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
    path('accounts/', include('accounts.urls', namespace = 'accounts')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
