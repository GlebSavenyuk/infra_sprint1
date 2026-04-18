from rest_framework import routers
from django.http import JsonResponse

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from cats.views import AchievementViewSet, CatViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', lambda request: JsonResponse({'message': 'API is working'})),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
