from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def hello_world(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path("api/v1/facechats/", include("facechats.urls")),
    path("api/v1/posts/", include("posts.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
    path("", hello_world)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
