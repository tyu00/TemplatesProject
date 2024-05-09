from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_site.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls'))
]

if settings.DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

