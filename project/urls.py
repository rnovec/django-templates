"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

# REST Framework
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from users.views import UserViewSet, home
from posts.views import PostViewSet

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.token import MyTokenObtainPairView

# API Router
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

# jwt urls
# http://domain.com/api/v1/token/...

jwt_urlpatterns = [
    path('social/', include('rest_social_auth.urls_jwt_pair')),
    path('access/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

docs = [
    # Swagger
    path('', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    # OpenAPI
    path('openapi/', get_schema_view(
        title="DRF API docs",
        version="1.0.0",
    ), name='openapi-schema'),
]

# api urls
# http://domain.com/api/v1/...

api_urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include(docs)),                
    path('token/', include(jwt_urlpatterns)),
    path('accounts/', include('rest_registration.api.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', home), 
    path('admin/', admin.site.urls), 
    path('api/v1/', include(api_urlpatterns)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
