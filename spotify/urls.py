
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny

from rest_framework.routers import DefaultRouter
from music.views import SongApiViewSet, AlbumAPIViewSet, ArtistAPIViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router =DefaultRouter()
router.register('song', SongApiViewSet)
router.register('album', AlbumAPIViewSet)
router.register('artist', ArtistAPIViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Spotify API",
      default_version='v1',
      description="Spotify music application",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bobojonovsiroj910@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[AllowAny],
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

