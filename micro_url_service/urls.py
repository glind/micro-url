"""micro_url_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework import permissions, routers


# openapi implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from micro_url.views import redirect_original

schema_view = get_schema_view(
    openapi.Info(
        title="Micro URL service",
        default_version='latest',
        description="URL shortener",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health_check/', include('health_check.urls')),
    re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/', include(router.urls)),
    re_path(r'^(?P<short_id>\w+)/$', redirect_original, name="redirect")
]

urlpatterns += staticfiles_urlpatterns()
