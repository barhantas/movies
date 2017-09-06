from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from moviesAPP.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^movie/', include('moviesAPP.urls')),
  ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
