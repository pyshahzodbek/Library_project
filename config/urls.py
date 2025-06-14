from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions  # TO‘G‘RI IMPORT

schema_view = get_schema_view(
    openapi.Info(
        title="Book list Api",
        default_version='v1',
        description='Library demo version',
        terms_of_service='demo.com',
        contact=openapi.Contact(email='shahzodravshanov123@gmail.com'),
        license=openapi.License(name='demo licence'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],  # TO‘G‘RI FOYDALANISH
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/',include('rest_framework.urls')),
        path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),


    # Swagger UI
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger-swagger-ui'),

    # ReDoc
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc')
]

