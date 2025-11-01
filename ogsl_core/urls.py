from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger / ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="OGSL API",
        default_version="v1",
        description="API OGSL (API-only)",
        contact=openapi.Contact(email="contact@ogsl.ca"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # 👉 rediriger la racine vers Swagger (évite de « chercher » une page d’accueil)
    path("", RedirectView.as_view(url="/swagger/", permanent=False)),

    # Admin (URL exacte : /admin/ — note bien le slash final)
    path("admin/", admin.site.urls),

    # API REST
    path("api/", include("catalog.urls")),

    # Swagger & ReDoc
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/",   schema_view.with_ui("redoc",   cache_timeout=0), name="schema-redoc"),
]
