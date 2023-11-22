from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('politicians/', include('politicians.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]


urlpatterns += i18n_patterns(
    path('politicians/', include('politicians.urls'))
)

# from dj_rest_auth.views import PasswordResetConfirmView

schema_view = get_schema_view(
    openapi.Info(
        title = 'Learn DRF',
        description = 'Project for learning DRF',
        default_version = 'v1',
        terms_of_service = 'https://programmer.uz/',
        contact = openapi.Contact(email='javohir0808@gmail.com', name='JAVOHIR', url='https://developer.com'),
        license = openapi.License(name='Hech qanaqa litsenziya'),
    ),
    public = True,
    permission_classes = (permissions.AllowAny, ),
    # docExpansion = 'none',
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/politicians/', include('app_politicians.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0,), name='schema-swagger-ui'),
    path('', schema_view.with_ui('swagger', cache_timeout=0,), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
#
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)